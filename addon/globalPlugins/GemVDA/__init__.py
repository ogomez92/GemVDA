# Gemini NVDA Add-on - Main Plugin
# -*- coding: utf-8 -*-

import os
import sys
import wx

import addonHandler
import globalPluginHandler
import config
import gui
import ui
import api
from scriptHandler import script
from gui.settingsDialogs import SettingsPanel, NVDASettingsDialog
from gui import guiHelper, nvdaControls
from logHandler import log

addonHandler.initTranslation()

from .consts import (
    DATA_DIR,
    LIBS_DIR,
    ADDON_DIR,
    NO_API_KEY_MSG,
    GEMINI_MODELS,
    DEFAULT_MODEL,
    DEFAULT_SYSTEM_PROMPT,
)
from .configspec import confSpecs
from . import apikeymanager
from . import videocapture

# Clear any conflicting modules that might be loaded from NVDA or other addons
# This includes typing_extensions which NVDA bundles an older version of
_modules_to_clear = [key for key in list(sys.modules.keys())
                     if key.startswith(('google.', 'pydantic', 'pydantic_core', 'typing_extensions', 'annotated_types'))]
for mod in _modules_to_clear:
    del sys.modules[mod]
# Also clear base modules if present
for base_mod in ('google', 'typing_extensions', 'annotated_types'):
    if base_mod in sys.modules:
        del sys.modules[base_mod]

# Add lib directory to path for google-genai (at the beginning for priority)
if LIBS_DIR in sys.path:
    sys.path.remove(LIBS_DIR)
sys.path.insert(0, LIBS_DIR)

# Try to import google-genai
try:
    from google import genai
    GENAI_AVAILABLE = True
    log.info(f"google-genai loaded successfully from {LIBS_DIR}")
except Exception as e:
    GENAI_AVAILABLE = False
    import traceback
    log.error(f"google-genai import failed: {e}")
    log.error(f"Full traceback:\n{traceback.format_exc()}")
    log.warning(
        "google-genai not found. Please run install_deps.py or install manually: "
        "pip install google-genai"
    )


class APIKeyDialog(wx.Dialog):
    """Dialog for entering Gemini API key."""

    def __init__(self, parent, key_manager: apikeymanager.APIKeyManager):
        # Translators: Title of API key configuration dialog
        super().__init__(parent, title=_("Gemini API Key"))
        self._key_manager = key_manager
        self._init_ui()
        self.CenterOnParent()

    def _init_ui(self):
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Instructions
        # Translators: Instructions for getting API key
        instructions = _(
            "Enter your Gemini API key.\n"
            "Get one at: https://aistudio.google.com/apikey"
        )
        instr_label = wx.StaticText(panel, label=instructions)
        sizer.Add(instr_label, 0, wx.ALL, 10)

        # Current key source
        source = self._key_manager.get_key_source()
        # Translators: Shows where API key is currently stored
        source_label = wx.StaticText(
            panel, label=_("Current key source: {source}").format(source=source)
        )
        sizer.Add(source_label, 0, wx.LEFT | wx.RIGHT, 10)

        # API key input
        key_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # Translators: Label for API key input field
        key_label = wx.StaticText(panel, label=_("API &Key:"))
        key_sizer.Add(key_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        self._key_text = wx.TextCtrl(panel, style=wx.TE_PASSWORD, size=(400, -1))
        current_key = self._key_manager.get_api_key() or ""
        if current_key:
            # Show masked key
            self._key_text.SetValue("*" * 20)
        key_sizer.Add(self._key_text, 1, wx.EXPAND)

        sizer.Add(key_sizer, 0, wx.EXPAND | wx.ALL, 10)

        # Buttons
        btn_sizer = wx.StdDialogButtonSizer()

        btn_ok = wx.Button(panel, wx.ID_OK)
        btn_ok.SetDefault()
        btn_sizer.AddButton(btn_ok)

        btn_cancel = wx.Button(panel, wx.ID_CANCEL)
        btn_sizer.AddButton(btn_cancel)

        # Translators: Button to delete saved API key
        btn_delete = wx.Button(panel, label=_("&Delete Key"))
        btn_delete.Bind(wx.EVT_BUTTON, self._on_delete)
        sizer.Add(btn_delete, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        btn_sizer.Realize()
        sizer.Add(btn_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(sizer)
        self.Fit()

        btn_ok.Bind(wx.EVT_BUTTON, self._on_ok)

    def _on_ok(self, event):
        key = self._key_text.GetValue().strip()
        # Don't save if it's the masked placeholder
        if key and not key.startswith("*" * 10):
            if self._key_manager.save_api_key(key):
                # Translators: Confirmation that API key was saved
                ui.message(_("API key saved"))
            else:
                # Translators: Error saving API key
                ui.message(_("Failed to save API key"))
        self.EndModal(wx.ID_OK)

    def _on_delete(self, event):
        if self._key_manager.delete_api_key():
            # Translators: Confirmation that API key was deleted
            ui.message(_("API key deleted"))
            self._key_text.SetValue("")
        else:
            # Translators: Error deleting API key
            ui.message(_("Failed to delete API key"))


class GeminiSettingsPanel(SettingsPanel):
    """Settings panel for Gemini add-on."""

    # Translators: Title of settings panel
    title = _("Gemini AI")

    def makeSettings(self, settingsSizer):
        sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

        # API Key section
        # Translators: Label for API key configuration button
        self._api_key_btn = sHelper.addItem(
            wx.Button(self, label=_("Configure API &Key..."))
        )
        self._api_key_btn.Bind(wx.EVT_BUTTON, self._on_configure_api_key)

        # Model selection
        model_choices = [m.name for m in GEMINI_MODELS]
        # Translators: Label for default model selection
        self._model_choice = sHelper.addLabeledControl(
            _("Default &model:"),
            wx.Choice,
            choices=model_choices,
        )
        current_model = config.conf["GemVDA"]["model"]
        for i, m in enumerate(GEMINI_MODELS):
            if m.id == current_model:
                self._model_choice.SetSelection(i)
                break

        # Temperature
        # Translators: Label for temperature setting
        self._temp_spinner = sHelper.addLabeledControl(
            _("&Temperature (0-200):"),
            nvdaControls.SelectOnFocusSpinCtrl,
            min=0,
            max=200,
        )
        self._temp_spinner.SetValue(int(config.conf["GemVDA"]["temperature"] * 100))

        # Max output tokens
        # Translators: Label for max output tokens setting
        self._max_tokens_spinner = sHelper.addLabeledControl(
            _("Ma&x output tokens:"),
            nvdaControls.SelectOnFocusSpinCtrl,
            min=1,
            max=65536,
        )
        self._max_tokens_spinner.SetValue(config.conf["GemVDA"]["maxOutputTokens"])

        # Streaming
        # Translators: Checkbox for streaming responses
        self._stream_checkbox = sHelper.addItem(
            wx.CheckBox(self, label=_("&Stream responses"))
        )
        self._stream_checkbox.SetValue(config.conf["GemVDA"]["stream"])

        # Conversation mode
        # Translators: Checkbox for conversation mode
        self._convo_checkbox = sHelper.addItem(
            wx.CheckBox(self, label=_("&Conversation mode (include history)"))
        )
        self._convo_checkbox.SetValue(config.conf["GemVDA"]["conversationMode"])

        # Save system prompt
        # Translators: Checkbox for saving system prompt
        self._save_prompt_checkbox = sHelper.addItem(
            wx.CheckBox(self, label=_("&Remember system prompt"))
        )
        self._save_prompt_checkbox.SetValue(config.conf["GemVDA"]["saveSystemPrompt"])

        # Block escape
        # Translators: Checkbox for blocking escape key
        self._block_escape_checkbox = sHelper.addItem(
            wx.CheckBox(self, label=_("&Block Escape key in dialog"))
        )
        self._block_escape_checkbox.SetValue(config.conf["GemVDA"]["blockEscapeKey"])

        # Filter markdown
        # Translators: Checkbox for filtering markdown from responses
        self._filter_markdown_checkbox = sHelper.addItem(
            wx.CheckBox(self, label=_("&Filter markdown from responses"))
        )
        self._filter_markdown_checkbox.SetValue(config.conf["GemVDA"]["filterMarkdown"])

        # Feedback section
        # Translators: Label for feedback settings group
        feedback_group = wx.StaticBoxSizer(
            wx.VERTICAL, self, label=_("Sound Feedback")
        )
        feedback_box = feedback_group.GetStaticBox()
        feedback_helper = guiHelper.BoxSizerHelper(self, sizer=feedback_group)

        # Translators: Checkbox for request sent sound
        self._snd_sent_checkbox = feedback_helper.addItem(
            wx.CheckBox(feedback_box, label=_("Play sound when request &sent"))
        )
        self._snd_sent_checkbox.SetValue(
            config.conf["GemVDA"]["feedback"]["soundRequestSent"]
        )

        # Translators: Checkbox for response pending sound
        self._snd_pending_checkbox = feedback_helper.addItem(
            wx.CheckBox(feedback_box, label=_("Play sound while &waiting"))
        )
        self._snd_pending_checkbox.SetValue(
            config.conf["GemVDA"]["feedback"]["soundResponsePending"]
        )

        # Translators: Checkbox for response received sound
        self._snd_received_checkbox = feedback_helper.addItem(
            wx.CheckBox(feedback_box, label=_("Play sound when response &received"))
        )
        self._snd_received_checkbox.SetValue(
            config.conf["GemVDA"]["feedback"]["soundResponseReceived"]
        )

        sHelper.addItem(feedback_group)

    def _on_configure_api_key(self, event):
        key_manager = apikeymanager.get_manager(DATA_DIR)
        dlg = APIKeyDialog(self, key_manager)
        dlg.ShowModal()
        dlg.Destroy()

    def onSave(self):
        # Model
        model_idx = self._model_choice.GetSelection()
        if model_idx >= 0:
            config.conf["GemVDA"]["model"] = GEMINI_MODELS[model_idx].id

        # Parameters
        config.conf["GemVDA"]["temperature"] = self._temp_spinner.GetValue() / 100.0
        config.conf["GemVDA"]["maxOutputTokens"] = self._max_tokens_spinner.GetValue()
        config.conf["GemVDA"]["stream"] = self._stream_checkbox.GetValue()
        config.conf["GemVDA"]["conversationMode"] = self._convo_checkbox.GetValue()
        config.conf["GemVDA"]["saveSystemPrompt"] = self._save_prompt_checkbox.GetValue()
        config.conf["GemVDA"]["blockEscapeKey"] = self._block_escape_checkbox.GetValue()
        config.conf["GemVDA"]["filterMarkdown"] = self._filter_markdown_checkbox.GetValue()

        # Feedback
        config.conf["GemVDA"]["feedback"]["soundRequestSent"] = (
            self._snd_sent_checkbox.GetValue()
        )
        config.conf["GemVDA"]["feedback"]["soundResponsePending"] = (
            self._snd_pending_checkbox.GetValue()
        )
        config.conf["GemVDA"]["feedback"]["soundResponseReceived"] = (
            self._snd_received_checkbox.GetValue()
        )


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """Global plugin for Gemini AI integration."""

    # Translators: Category for input gestures
    scriptCategory = _("Gemini AI")

    def __init__(self):
        super().__init__()

        # Register configuration
        config.conf.spec["GemVDA"] = confSpecs

        # Register settings panel
        NVDASettingsDialog.categoryClasses.append(GeminiSettingsPanel)

        # Initialize API key manager
        self._key_manager = apikeymanager.get_manager(DATA_DIR)

        # Client instance (lazy loaded)
        self._client = None

        # Video capture instance
        self._video_capture = None

        # Clean up old temporary files on startup
        self._cleanup_temp_files()

        # Create menu
        self._create_menu()

        log.info("Gemini add-on initialized")

    def _cleanup_temp_files(self):
        """Clean up old screenshot and video files on startup."""
        import glob

        patterns = [
            os.path.join(DATA_DIR, "screenshot_*.png"),
            os.path.join(DATA_DIR, "object_*.png"),
            os.path.join(DATA_DIR, "capture_*.mp4"),
        ]

        deleted_count = 0
        for pattern in patterns:
            for filepath in glob.glob(pattern):
                try:
                    os.remove(filepath)
                    deleted_count += 1
                except Exception as e:
                    log.warning(f"Failed to delete temp file {filepath}: {e}")

        if deleted_count > 0:
            log.info(f"Cleaned up {deleted_count} temporary files from previous session")

    def terminate(self):
        """Clean up when add-on is disabled/NVDA exits."""
        # Stop video capture if running
        if self._video_capture and self._video_capture.is_recording:
            self._video_capture.stop()

        # Remove settings panel
        try:
            NVDASettingsDialog.categoryClasses.remove(GeminiSettingsPanel)
        except ValueError:
            pass

        # Remove menu
        try:
            gui.mainFrame.sysTrayIcon.menu.Remove(self._menu_item)
        except Exception:
            pass

        log.info("Gemini add-on terminated")

    def _create_menu(self):
        """Create system tray menu item."""
        self._menu = wx.Menu()

        # Translators: Menu item to open Gemini dialog
        dialog_item = self._menu.Append(wx.ID_ANY, _("Open Gemini &Dialog...\tNVDA+G"))
        gui.mainFrame.sysTrayIcon.Bind(
            wx.EVT_MENU, self._on_show_dialog, dialog_item
        )

        self._menu.AppendSeparator()

        # Translators: Menu item to open settings
        settings_item = self._menu.Append(wx.ID_ANY, _("&Settings..."))
        gui.mainFrame.sysTrayIcon.Bind(
            wx.EVT_MENU, self._on_show_settings, settings_item
        )

        # Translators: Menu item to open API key page
        api_item = self._menu.Append(wx.ID_ANY, _("Get &API Key (web)..."))
        gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self._on_open_api_page, api_item)

        # Add to system tray
        # Translators: System tray menu item label
        self._menu_item = gui.mainFrame.sysTrayIcon.menu.Insert(
            2, wx.ID_ANY, _("&Gemini"), self._menu
        )

    def _on_show_dialog(self, event):
        """Open the main Gemini dialog."""
        self._show_dialog()

    def _on_show_settings(self, event):
        """Open settings panel."""
        wx.CallAfter(
            gui.mainFrame.popupSettingsDialog,
            NVDASettingsDialog,
            GeminiSettingsPanel,
        )

    def _on_open_api_page(self, event):
        """Open API key page in browser."""
        import webbrowser
        webbrowser.open("https://aistudio.google.com/apikey")

    def _get_client(self):
        """Get or create Gemini client."""
        if not GENAI_AVAILABLE:
            return None

        api_key = self._key_manager.get_api_key()
        if not api_key:
            return None

        if self._client is None:
            try:
                self._client = genai.Client(api_key=api_key)
            except Exception as e:
                log.error(f"Failed to create Gemini client: {e}")
                return None

        return self._client

    def _show_dialog(self):
        """Show the main Gemini dialog."""
        if not GENAI_AVAILABLE:
            # Translators: Error when google-genai is not installed
            ui.message(
                _(
                    "Google GenAI library not installed. "
                    "Please run install_deps.py in the add-on folder."
                )
            )
            return

        client = self._get_client()
        if not client:
            ui.message(_(NO_API_KEY_MSG))
            return

        from . import maindialog

        # Check if dialog already open
        if (
            maindialog.addToSession
            and isinstance(maindialog.addToSession, maindialog.GeminiDialog)
        ):
            maindialog.addToSession.Raise()
            maindialog.addToSession.SetFocus()
            return

        wx.CallAfter(self._open_dialog, client)

    def _open_dialog(self, client):
        """Open dialog on main thread."""
        from . import maindialog

        dlg = maindialog.GeminiDialog(
            gui.mainFrame,
            client=client,
            conf_ref=config.conf,
        )
        dlg.Show()
        dlg.Raise()
        dlg.SetFocus()
        # Ensure the prompt field gets focus
        wx.CallAfter(dlg.focus_prompt)

    def _capture_screenshot(self, scale: float = 0.5) -> str | None:
        """Capture full screen and return path to image.

        Args:
            scale: Scale factor to reduce resolution (0.5 = half size)
        """
        try:
            # Add mss to path if available
            if LIBS_DIR not in sys.path:
                sys.path.insert(0, LIBS_DIR)

            import mss
            import datetime
            from PIL import Image

            now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(DATA_DIR, f"screenshot_{now}.png")

            with mss.mss() as sct:
                # Capture primary monitor
                img = sct.grab(sct.monitors[1])
                # Convert to PIL Image
                pil_img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

                # Resize to reduce file size
                if scale < 1.0:
                    new_size = (int(pil_img.width * scale), int(pil_img.height * scale))
                    pil_img = pil_img.resize(new_size, Image.Resampling.LANCZOS)

                # Save with compression
                pil_img.save(path, "PNG", optimize=True)

            return path
        except ImportError:
            log.warning("mss not available for screenshots")
            return None
        except Exception as e:
            log.error(f"Screenshot failed: {e}")
            return None

    def _capture_object(self, scale: float = 0.75) -> str | None:
        """Capture navigator object and return path to image.

        Args:
            scale: Scale factor to reduce resolution (0.75 = 75% size)
        """
        try:
            if LIBS_DIR not in sys.path:
                sys.path.insert(0, LIBS_DIR)

            import mss
            import datetime
            from PIL import Image

            nav = api.getNavigatorObject()
            if not nav or not nav.location:
                return None

            nav.scrollIntoView()
            loc = nav.location

            now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(DATA_DIR, f"object_{now}.png")

            monitor = {
                "top": loc.top,
                "left": loc.left,
                "width": loc.width,
                "height": loc.height,
            }

            with mss.mss() as sct:
                img = sct.grab(monitor)
                pil_img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

                # Resize to reduce file size (only if image is large enough)
                if scale < 1.0 and pil_img.width > 100 and pil_img.height > 100:
                    new_size = (int(pil_img.width * scale), int(pil_img.height * scale))
                    pil_img = pil_img.resize(new_size, Image.Resampling.LANCZOS)

                # Save with compression
                pil_img.save(path, "PNG", optimize=True)

            return path
        except ImportError as e:
            log.warning(f"Dependencies not available for object capture: {e}")
            return None
        except Exception as e:
            log.error(f"Object capture failed: {e}")
            return None

    @script(
        # Translators: Description for show dialog script
        description=_("Show Gemini AI dialog"),
        gesture="kb:nvda+g",
    )
    def script_showDialog(self, gesture):
        self._show_dialog()

    @script(
        # Translators: Description for describe screen script
        description=_("Describe the entire screen using Gemini"),
        gesture="kb:nvda+shift+e",
    )
    def script_describeScreen(self, gesture):
        if not GENAI_AVAILABLE:
            ui.message(_("Google GenAI library not installed."))
            return

        client = self._get_client()
        if not client:
            ui.message(_(NO_API_KEY_MSG))
            return

        # Translators: Message while capturing screenshot
        ui.message(_("Capturing screen..."))

        path = self._capture_screenshot()
        if not path:
            # Translators: Error when screenshot fails
            ui.message(_("Failed to capture screenshot"))
            return

        from . import maindialog

        if maindialog.addToSession:
            maindialog.addToSession.add_images([path], prompt_type="screenshot")
        else:
            self._open_dialog(client)
            wx.CallLater(500, lambda: self._add_image_to_dialog(path, "screenshot"))

    def _add_image_to_dialog(self, path, prompt_type=None):
        from . import maindialog
        if maindialog.addToSession:
            maindialog.addToSession.add_images([path], prompt_type=prompt_type)

    @script(
        # Translators: Description for describe object script
        description=_("Describe the navigator object using Gemini"),
        gesture="kb:nvda+shift+o",
    )
    def script_describeObject(self, gesture):
        if not GENAI_AVAILABLE:
            ui.message(_("Google GenAI library not installed."))
            return

        client = self._get_client()
        if not client:
            ui.message(_(NO_API_KEY_MSG))
            return

        # Translators: Message while capturing object
        ui.message(_("Capturing object..."))

        path = self._capture_object()
        if not path:
            # Translators: Error when object capture fails
            ui.message(_("Failed to capture object"))
            return

        from . import maindialog

        if maindialog.addToSession:
            maindialog.addToSession.add_images([path], prompt_type="object")
        else:
            self._open_dialog(client)
            wx.CallLater(500, lambda: self._add_image_to_dialog(path, "object"))

    def _get_video_capture(self):
        """Get or create video capture instance."""
        if self._video_capture is None:
            self._video_capture = videocapture.VideoCapture(DATA_DIR)
        return self._video_capture

    def _analyze_video(self, video_path: str):
        """Send video to Gemini for analysis in a background thread."""
        import threading

        def do_analysis():
            try:
                client = self._get_client()
                if not client:
                    wx.CallAfter(ui.message, _(NO_API_KEY_MSG))
                    return

                # Import types for proper API formatting
                from google.genai import types

                # Upload video file
                # Translators: Message while uploading video
                wx.CallAfter(ui.message, _("Uploading video..."))

                uploaded_file = client.files.upload(
                    file=video_path,
                    config={"mime_type": "video/mp4"},
                )

                # Wait for processing
                import time
                while uploaded_file.state.name == "PROCESSING":
                    time.sleep(1)
                    uploaded_file = client.files.get(name=uploaded_file.name)

                if uploaded_file.state.name == "FAILED":
                    wx.CallAfter(ui.message, _("Video processing failed"))
                    return

                # Translators: Message while analyzing video
                wx.CallAfter(ui.message, _("Analyzing video..."))

                # Get model from config
                model_id = config.conf["GemVDA"]["model"]

                # Create content with video and prompt
                response = client.models.generate_content(
                    model=model_id,
                    contents=[
                        types.Content(
                            role="user",
                            parts=[
                                types.Part.from_uri(
                                    file_uri=uploaded_file.uri,
                                    mime_type="video/mp4",
                                ),
                                types.Part(text=videocapture.VIDEO_ANALYSIS_PROMPT),
                            ],
                        )
                    ],
                )

                # Get the response text
                result_text = response.text if response.text else _("No response from AI")

                # Apply markdown filter if enabled
                if config.conf["GemVDA"]["filterMarkdown"]:
                    from .mdfilter import filter_markdown
                    result_text = filter_markdown(result_text)

                # Announce result
                wx.CallAfter(ui.message, result_text)

                # Clean up uploaded file
                try:
                    client.files.delete(name=uploaded_file.name)
                except Exception:
                    pass

                # Clean up local video file
                try:
                    os.remove(video_path)
                except Exception:
                    pass

            except Exception as e:
                log.error(f"Video analysis failed: {e}", exc_info=True)
                # Translators: Error during video analysis
                wx.CallAfter(
                    ui.message,
                    _("Video analysis failed: {error}").format(error=str(e))
                )

        thread = threading.Thread(target=do_analysis, daemon=True)
        thread.start()

    @script(
        # Translators: Description for video capture toggle script
        description=_("Start or stop video recording for Gemini analysis"),
        gesture="kb:nvda+v",
    )
    def script_toggleVideoCapture(self, gesture):
        if not GENAI_AVAILABLE:
            ui.message(_("Google GenAI library not installed."))
            return

        capture = self._get_video_capture()

        if not capture.is_available:
            # Translators: Error when video capture dependencies not available
            ui.message(_("Video capture not available. Missing dependencies."))
            return

        if capture.is_recording:
            # Stop recording
            # Translators: Message when stopping video recording
            ui.message(_("Stopping recording..."))
            video_path = capture.stop()

            if video_path:
                # Translators: Message when video saved successfully
                ui.message(_("Video saved. Sending to Gemini for analysis..."))
                self._analyze_video(video_path)
            else:
                # Translators: Error when video save fails
                ui.message(_("Failed to save video"))
        else:
            # Start recording
            if capture.start():
                # Translators: Message when video recording starts
                ui.message(_("Recording started. Press NVDA+V again to stop."))
            else:
                # Translators: Error when video recording fails to start
                ui.message(_("Failed to start recording"))
