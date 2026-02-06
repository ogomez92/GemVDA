# Gemini NVDA Add-on - Configuration Specification
# -*- coding: utf-8 -*-

import re

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

    # Video analysis prompt (empty = use localized default)
    "videoPrompt": 'string(default="")',

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


def _parse_default(spec_string):
    """Extract the default value from a configobj spec string."""
    m = re.search(r"default=(['\"])(.*?)\1", spec_string)
    if m:
        return m.group(2)
    m = re.search(r"default=(\S+)", spec_string)
    if m:
        raw = m.group(1).rstrip(",)")
        if spec_string.startswith("boolean"):
            return raw.lower() == "true"
        if spec_string.startswith("integer"):
            return int(raw)
        if spec_string.startswith("float"):
            return float(raw)
        return raw
    return None


def _build_defaults(specs):
    """Build a nested dict of default values from confSpecs."""
    result = {}
    for key, value in specs.items():
        if isinstance(value, dict):
            result[key] = _build_defaults(value)
        else:
            result[key] = _parse_default(value)
    return result


_DEFAULTS = _build_defaults(confSpecs)


class _SafeSection:
    """Wraps an NVDA config section, falling back to confSpec defaults on KeyError."""

    def __init__(self, conf_section, defaults):
        self._conf = conf_section
        self._defaults = defaults

    def __getitem__(self, key):
        try:
            val = self._conf[key]
        except KeyError:
            if key not in self._defaults:
                raise
            val = self._defaults[key]
        # Wrap sub-sections so nested access is also safe
        sub_defaults = self._defaults.get(key, {})
        if isinstance(sub_defaults, dict) and sub_defaults:
            if not isinstance(val, (str, bytes, bool, int, float, type(None))):
                return _SafeSection(val, sub_defaults)
        return val

    def __setitem__(self, key, value):
        self._conf[key] = value

    def __contains__(self, key):
        return key in self._conf or key in self._defaults

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


def get_safe_conf():
    """Get the GemVDA config section with safe fallback to spec defaults.

    Use this instead of config.conf["GemVDA"] to avoid KeyError when
    NVDA's config profiles don't have the expected keys.
    """
    import config
    try:
        section = config.conf["GemVDA"]
    except KeyError:
        return _SafeSection(type('Empty', (), {
            '__getitem__': lambda s, k: (_ for _ in ()).throw(KeyError(k)),
            '__setitem__': lambda s, k, v: None,
            '__contains__': lambda s, k: False,
        })(), _DEFAULTS)
    return _SafeSection(section, _DEFAULTS)
