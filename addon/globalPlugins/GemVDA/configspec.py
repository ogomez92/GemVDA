# Gemini NVDA Add-on - Configuration Specification
# -*- coding: utf-8 -*-

confSpecs = {
    # Model settings
    "model": "string(default='gemini-2.5-flash')",
    "modelVision": "string(default='gemini-2.5-flash')",

    # Generation parameters
    "temperature": "float(min=0.0, max=2.0, default=1.0)",
    "topP": "float(min=0.0, max=1.0, default=0.95)",
    "topK": "integer(min=1, max=100, default=40)",
    "maxOutputTokens": "integer(min=1, max=65536, default=8192)",
    "stream": "boolean(default=True)",

    # Conversation settings
    "conversationMode": "boolean(default=True)",
    "saveSystemPrompt": "boolean(default=True)",
    "customSystemPrompt": 'string(default="")',

    # UI settings
    "blockEscapeKey": "boolean(default=False)",
    "advancedMode": "boolean(default=False)",
    "filterMarkdown": "boolean(default=True)",

    # Saved prompts for image descriptions
    "screenshotPrompt": 'string(default="")',
    "objectPrompt": 'string(default="")',

    # Image settings
    "images": {
        "resize": "boolean(default=True)",
        "maxWidth": "integer(min=0, max=4096, default=1024)",
        "maxHeight": "integer(min=0, max=4096, default=1024)",
        "quality": "integer(min=1, max=100, default=85)",
        "useCustomPrompt": "boolean(default=False)",
        "customPromptText": 'string(default="")',
    },

    # Feedback settings
    "feedback": {
        "soundRequestSent": "boolean(default=True)",
        "soundResponsePending": "boolean(default=True)",
        "soundResponseReceived": "boolean(default=True)",
        "speechResponseReceived": "boolean(default=True)",
        "brailleAutoFocus": "boolean(default=True)",
    },

    # Debug
    "debug": "boolean(default=False)",
}
