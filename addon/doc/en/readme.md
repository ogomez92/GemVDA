# GemVDA - Google Gemini AI for NVDA

## Summary

GemVDA integrates Google Gemini AI capabilities directly into NVDA, providing blind and visually impaired users with powerful AI assistance. The add-on supports various Gemini models including Gemini 3, Gemini 2.5 Pro and Flash variants for chat, image description, video analysis and more.

## Features

* **AI Chat**: Have conversations with Gemini AI directly from NVDA
* **Screen Description**: Capture and describe the entire screen
* **Object Description**: Describe the current navigator object
* **Video Analysis**: Record screen video and have Gemini analyze it
* **Attach Images**: Attach images from files for AI description
* **Conversation History**: Maintain context across multiple messages
* **Multiple Models**: Choose from various Gemini models based on your needs
* **Customizable Settings**: Configure temperature, tokens, streaming and more

## Requirements

* NVDA 2023.1 or later
* Google Gemini API key (free tier available)
* Internet connection

## Setup

### Getting an API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to use in the add-on

### Configuring the API Key

1. Press NVDA+N to open the NVDA menu
2. Go to Preferences > Settings
3. Select the "Gemini AI" category
4. Click "Configure API key..."
5. Paste your API key and press OK

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| NVDA+G | Open Gemini AI dialog |
| NVDA+Shift+E | Describe the entire screen |
| NVDA+Shift+O | Describe the navigator object |
| NVDA+V | Start/stop video recording for analysis |

## Using the Gemini Dialog

When you open the Gemini dialog with NVDA+G:

1. **Model**: Select which Gemini model to use
2. **System Prompt**: Optional instructions on how Gemini should respond
3. **History**: View the conversation history
4. **Message**: Type your message or question
5. **Send**: Send your message to Gemini
6. **Attach Image**: Add an image file for Gemini to analyze
7. **Clear**: Clear the conversation history
8. **Copy Response**: Copy the last response to the clipboard

### Dialog Tips

* Press ctrl+enter in the message field to quickly send
* Use Tab to navigate between controls
* History updates automatically as you chat
* Attached images are sent with your next message

## Settings

Access settings via NVDA menu > Preferences > Settings > Gemini AI:

* **Default Model**: Choose your preferred Gemini model
* **Temperature (0-200)**: Controls response creativity (0=focused, 200=creative)
* **Maximum Output Tokens**: Maximum length of responses
* **Stream Responses**: Display responses as they arrive
* **Conversation Mode**: Include chat history for context
* **Remember System Prompt**: Save your custom prompt
* **Block Escape Key**: Prevent accidental dialog closure
* **Filter Markdown**: Remove markdown formatting from responses

### Audio Feedback

* **Play sound when sending request**: Audio confirmation when message is sent
* **Play sound while waiting**: Progress sound during AI processing
* **Play sound when response received**: Notification when response arrives

## Available Models

* **Gemini 3 Pro (Preview)**: Most capable model with reasoning capabilities
* **Gemini 3 Flash (Preview)**: Fast model with reasoning capabilities
* **Gemini 2.5 Pro**: Powerful production-ready model
* **Gemini 2.5 Flash**: Fast and efficient for most tasks
* **Gemini 2.5 Flash-Lite**: Lightweight and faster responses
* **Gemini 2.5 Flash Image**: Optimized for image-related tasks

## Image and Video Features

### Screen Description (NVDA+Shift+E)

Captures your entire screen and sends it to Gemini for a detailed description. Useful for:

* Understanding unfamiliar interfaces
* Getting an overview of visual content
* Identifying elements that NVDA cannot describe

### Object Description (NVDA+Shift+O)

Captures only the current navigator object. Useful for:

* Describing specific interface elements
* Understanding images or icons
* Getting details about focused controls

### Video Analysis (NVDA+V)

1. Press NVDA+V to start recording
2. Perform the actions you want to analyze
3. Press NVDA+V again to stop
4. Wait for Gemini to analyze the video

Useful for:

* Understanding visual workflows
* Getting step-by-step descriptions
* Analyzing dynamic content

## Troubleshooting

### "Google GenAI library not installed"

Run the dependency installer:
1. Navigate to %APPDATA%\nvda\addons\GemVDA
2. Run install_deps.bat or install_deps.py
3. Restart NVDA

### "No API key configured"

Configure your API key in Settings > Gemini AI > Configure API key

### Responses are too short or cut off

Increase the "Maximum Output Tokens" setting

### Responses are too random

Lower the Temperature setting (try 50-100)

## Privacy Notice

* Your messages and images are sent to Google's Gemini API
* API keys are stored locally in your NVDA configuration
* No data is shared with the add-on developer
* Review Google's AI privacy policy for more details

## Support

* Report issues: [GitHub Issues](https://github.com/ogomez92/GemVDA/issues)
* Source code: [GitHub Repository](https://github.com/ogomez92/GemVDA)

## License

This add-on is released under the GNU General Public License v2.

## Author

Oriol Gomez Sentis
