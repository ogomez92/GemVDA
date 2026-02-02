# GemVDA NVDA Add-on - Installation Tasks
# -*- coding: utf-8 -*-
"""
This module runs during add-on installation and uninstallation.
"""

import os
from logHandler import log


def onInstall():
    """Called when the add-on is installed."""
    log.info("GemVDA add-on installed")

    # Check if dependencies are installed
    addon_dir = os.path.dirname(__file__)
    lib_dir = os.path.join(addon_dir, "lib")

    if not os.path.exists(lib_dir) or not os.listdir(lib_dir):
        # Dependencies not installed - show message
        import gui
        import wx

        wx.CallAfter(
            gui.messageBox,
            "GemVDA add-on installed successfully!\n\n"
            "IMPORTANT: You need to install dependencies before using this add-on.\n\n"
            "Run install_deps.bat or install_deps.py in the add-on folder:\n"
            "%APPDATA%\\nvda\\addons\\GemVDA\n\n"
            "Then restart NVDA.",
            "GemVDA Add-on - Setup Required",
            wx.OK | wx.ICON_INFORMATION,
        )


def onUninstall():
    """Called when the add-on is uninstalled."""
    log.info("GemVDA add-on uninstalled")

    # Clean up configuration
    try:
        import config

        if "GemVDA" in config.conf:
            del config.conf["GemVDA"]
    except Exception as e:
        log.warning(f"Could not clean up config: {e}")

    # Clean up data directory
    try:
        import globalVars
        import shutil

        data_dir = os.path.join(globalVars.appArgs.configPath, "GemVDA")
        if os.path.exists(data_dir):
            # Ask user if they want to keep their data
            import gui
            import wx

            result = gui.messageBox(
                "Do you want to delete your GemVDA add-on data?\n"
                "(API key and conversation history)",
                "GemVDA Add-on Uninstall",
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION,
            )

            if result == wx.YES:
                shutil.rmtree(data_dir)
                log.info("GemVDA data directory deleted")
    except Exception as e:
        log.warning(f"Could not clean up data: {e}")
