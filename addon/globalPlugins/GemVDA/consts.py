# Gemini NVDA Add-on - Constants and Model Definitions
# -*- coding: utf-8 -*-

import os
import globalVars

# Directory paths
ADDON_DIR = os.path.dirname(__file__)
PLUGIN_DIR = os.path.dirname(ADDON_DIR)
ADDON_ROOT = os.path.dirname(PLUGIN_DIR)
DATA_DIR = os.path.join(globalVars.appArgs.configPath, "GemVDA")
LIBS_DIR = os.path.join(ADDON_ROOT, "lib")

# Create data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Sound files
SOUNDS_DIR = os.path.join(ADDON_DIR, "sounds")
SND_CHAT_REQUEST_SENT = os.path.join(SOUNDS_DIR, "chatRequestSent.wav")
SND_CHAT_RESPONSE_PENDING = os.path.join(SOUNDS_DIR, "chatResponsePending.wav")
SND_CHAT_RESPONSE_RECEIVED = os.path.join(SOUNDS_DIR, "chatResponseReceived.wav")
SND_PROGRESS = os.path.join(SOUNDS_DIR, "progress.wav")

# Default system prompt for accessibility
DEFAULT_SYSTEM_PROMPT = """You are a helpful AI assistant integrated with NVDA, a screen reader for blind and visually impaired users.

When describing visual content:
- Be thorough and descriptive, as users cannot see the content
- Describe layout, colors, text, and important visual elements
- For images, describe what you see in detail
- For UI elements, explain their purpose and current state

When providing information:
- Be concise but complete
- Use clear, accessible language
- Avoid unnecessary visual references like "as you can see"
- Structure information logically for audio consumption

For code and technical content:
- Explain code structure and logic clearly
- Mention indentation and nesting levels when relevant
- Describe error messages and their likely causes
"""

# Gemini model definitions
class Model:
    """Represents a Gemini model with its capabilities."""

    def __init__(
        self,
        id: str,
        name: str,
        context_window: int = 1000000,
        max_output_tokens: int = 8192,
        max_temperature: float = 2.0,
        vision: bool = False,
        preview: bool = False,
        thinking: bool = False,
    ):
        self.id = id
        self.name = name
        self.context_window = context_window
        self.max_output_tokens = max_output_tokens
        self.max_temperature = max_temperature
        self.vision = vision
        self.preview = preview
        self.thinking = thinking

    def __repr__(self):
        return f"Model({self.id}, vision={self.vision})"


# Available Gemini models (as of early 2026)
GEMINI_MODELS = [
    # Gemini 3 models (Preview)
    Model(
        id="gemini-3-pro-preview",
        name="Gemini 3 Pro (Preview)",
        context_window=1000000,
        max_output_tokens=65536,
        vision=True,
        preview=True,
        thinking=True,
    ),
    Model(
        id="gemini-3-flash-preview",
        name="Gemini 3 Flash (Preview)",
        context_window=1000000,
        max_output_tokens=32768,
        vision=True,
        preview=True,
        thinking=True,
    ),
    # Gemini 2.5 models (Production)
    Model(
        id="gemini-2.5-pro",
        name="Gemini 2.5 Pro",
        context_window=1000000,
        max_output_tokens=65536,
        vision=True,
        thinking=True,
    ),
    Model(
        id="gemini-2.5-flash",
        name="Gemini 2.5 Flash",
        context_window=1000000,
        max_output_tokens=8192,
        vision=True,
    ),
    Model(
        id="gemini-2.5-flash-lite",
        name="Gemini 2.5 Flash-Lite",
        context_window=1000000,
        max_output_tokens=8192,
        vision=True,
    ),
    # Image generation model
    Model(
        id="gemini-2.5-flash-image",
        name="Gemini 2.5 Flash Image",
        context_window=32000,
        max_output_tokens=8192,
        vision=True,
    ),
]

# Default model
DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_VISION_MODEL = "gemini-2.5-flash"

# Model lookup helpers
def get_model_by_id(model_id: str) -> Model | None:
    """Get a model by its ID."""
    for model in GEMINI_MODELS:
        if model.id == model_id:
            return model
    return None

def get_model_choices() -> list[tuple[str, str]]:
    """Get list of (id, name) tuples for UI choices."""
    return [(m.id, m.name) for m in GEMINI_MODELS]

def get_vision_models() -> list[Model]:
    """Get models with vision capability."""
    return [m for m in GEMINI_MODELS if m.vision]

# Default prompts for image descriptions
DEFAULT_SCREENSHOT_PROMPT = "Describe this screenshot in detail. What application or content is shown? What are the main elements visible on screen?"

DEFAULT_OBJECT_PROMPT = "Describe this UI element or object in detail. What is it? What does it show or do?"

# Error messages
NO_API_KEY_MSG = "No Gemini API key configured. Please add your API key in the settings."
API_ERROR_MSG = "Error communicating with Gemini API: {error}"
