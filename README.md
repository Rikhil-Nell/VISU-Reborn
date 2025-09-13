# 🤖 VISU-Reborn

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LiveKit](https://img.shields.io/badge/LiveKit-Agents-green.svg)](https://docs.livekit.io/agents/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> An emotionally intelligent voice assistant with real-time emotion detection and visual feedback

VISU is an advanced voice assistant that combines conversational AI with emotional intelligence. It detects user emotions, responds empathetically, and provides real-time visual feedback through a modern web interface.

## ✨ Features

### 🎭 **Emotional Intelligence**
- **Real-time emotion detection** - Analyzes user sentiment and responds appropriately
- **Empathetic responses** - Matches user's emotional state (sad → empathetic, happy → excited)
- **8 emotion types** - Happy, curious, empathetic, neutral, excited, concerned, supportive, playful
- **Visual feedback** - Live emotion display with colors and animations

### 🗣️ **Voice Capabilities**
- **Natural conversation** - Powered by advanced language models (GPT/Cerebras)
- **High-quality TTS** - Cartesia voice synthesis
- **Accurate STT** - Deepgram speech recognition
- **Voice activity detection** - Silero VAD for seamless interaction

### 🌐 **Real-time Frontend**
- **Live emotion display** - WebSocket-powered real-time updates
- **Modern UI** - Glassmorphism design with smooth animations
- **Responsive design** - Works on desktop and mobile
- **Connection resilience** - Auto-reconnection and error handling

### 🔧 **Architecture**
- **Modular design** - Separate agent, context, and frontend components
- **Configuration management** - Environment-based settings
- **Error handling** - Robust fallback mechanisms
- **Extensible** - Easy to add new emotions, tools, and features

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js (optional, for advanced frontend development)
- API keys for:
  - OpenAI/Cerebras (LLM)
  - Deepgram (Speech-to-Text)
  - Cartesia (Text-to-Speech)
  - LiveKit (Real-time communication)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbhiramVSA/VISU-Reborn.git
   cd VISU-Reborn
   ```

2. **Set up Python environment**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

   Required environment variables:
   ```env
   OPENAI_API_KEY=your_openai_key
   DEEPGRAM_API_KEY=your_deepgram_key
   CARTESIA_API_KEY=your_cartesia_key
   LIVEKIT_API_KEY=your_livekit_key
   LIVEKIT_API_SECRET=your_livekit_secret
   LIVEKIT_URL=your_livekit_url
   ```

4. **Start the emotion frontend**
   ```bash
   cd frontend
   python server.py
   ```

5. **Run the voice assistant**
   ```bash
   # In a new terminal
   uv run main.py
   ```

6. **Open the emotion display**
   - Visit http://localhost:8000 in your browser
   - You'll see real-time emotion updates as you interact with VISU

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Voice Input   │───▶│   VISU Agent     │───▶│  Emotion API    │
│   (Microphone)  │    │  - LLM Processing│    │  (HTTP POST)    │
└─────────────────┘    │  - Emotion Det.  │    └─────────────────┘
                       │  - Response Gen. │              │
┌─────────────────┐    │  - TTS Output    │              ▼
│  Voice Output   │◀───│                  │    ┌─────────────────┐
│   (Speakers)    │    └──────────────────┘    │  Web Frontend   │
└─────────────────┘                            │  - Live Display │
                                               │  - WebSocket    │
                                               │  - Animations   │
                                               └─────────────────┘
```

### Core Components

- **`agent/visu.py`** - Main voice assistant with emotion detection
- **`frontend/server.py`** - FastAPI server for emotion visualization
- **`context/`** - Context loading and management
- **`config/`** - Configuration and environment management
- **`prompts/`** - AI personality and behavior rules

## 🎭 Emotion System

VISU recognizes and responds to user emotions with appropriate emotional states:

| User Emotion | VISU Response | Visual Color | Emoji |
|--------------|---------------|--------------|-------|
| **Sad** | Empathetic, Concerned | Purple, Orange | 🤗 😟 |
| **Happy** | Excited, Joyful | Gold, Red | 😊 🤩 |
| **Angry** | Calming, Supportive | Green | 🫂 |
| **Confused** | Patient, Helpful | Blue | 🤔 |
| **Neutral** | Friendly | Light Gray | 😐 |

## 🔧 Configuration

### Environment Setup
Create a `.env` file in the root directory:

```env
# Required API Keys
OPENAI_API_KEY=sk-...
DEEPGRAM_API_KEY=...
CARTESIA_API_KEY=sk_car_...
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
LIVEKIT_URL=wss://...
```

### Customizing VISU's Personality
Edit the prompt files to customize VISU's behavior:

- **`prompts/prompt.txt`** - Core personality and speaking style
- **`prompts/rules.txt`** - Operational rules and constraints

### Adding Context
Place text files in the `context/` directory to give VISU additional knowledge.

## 🧪 Development

### Project Structure
```
VISU-Reborn/
├── agent/              # Voice assistant core
│   ├── visu.py        # Main agent implementation
│   └── __init__.py
├── frontend/          # Emotion visualization
│   ├── server.py      # FastAPI backend
│   ├── requirements.txt
│   └── README.md
├── context/           # Knowledge base
│   ├── context.py     # Context loader
│   └── *.txt         # Context files
├── config/            # Configuration
│   └── settings.py    # Environment management
├── prompts/           # AI personality
│   ├── prompt.txt     # Core personality
│   └── rules.txt      # Behavioral rules
├── main.py           # Entry point
├── pyproject.toml    # Python dependencies
└── .env             # Environment variables
```

### Running Tests
```bash
# Run frontend tests
cd frontend
python -m pytest

# Run agent tests
python -m pytest tests/
```

### Code Quality
```bash
# Format code
black .
isort .

# Lint code
flake8 .
pylint agent/ frontend/
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### 🚀 Quick Contribution Guide

1. **Fork the repository**
   ```bash
   git fork https://github.com/AbhiramVSA/VISU-Reborn.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new features
   - Update documentation as needed

4. **Test your changes**
   ```bash
   # Test the agent
   uv run main.py
   
   # Test the frontend
   cd frontend && python server.py
   ```

5. **Commit and push**
   ```bash
   git commit -m "feat: add amazing feature"
   git push origin feature/amazing-feature
   ```

6. **Create a Pull Request**
   - Use the PR template
   - Describe your changes clearly
   - Link related issues

### 🎯 Contribution Areas

#### 🎭 **Emotion System**
- Add new emotion types
- Improve emotion detection accuracy
- Create emotion transition animations

#### 🗣️ **Voice Capabilities**
- Add support for different languages
- Improve voice recognition accuracy
- Add voice cloning features

#### 🌐 **Frontend Enhancements**
- Create mobile app version
- Add emotion history graphs
- Implement theme customization

#### 🔧 **Technical Improvements**
- Add comprehensive testing
- Improve error handling
- Optimize performance
- Add Docker support

#### 📚 **Documentation**
- Write tutorials
- Create API documentation
- Add video demos

### 📋 Development Guidelines

#### Code Style
- Use **Black** for Python formatting
- Follow **PEP 8** conventions
- Write descriptive commit messages
- Add docstrings to all functions

#### Testing
- Write unit tests for new features
- Test voice interaction manually
- Verify frontend functionality
- Check emotion detection accuracy

#### Documentation
- Update README for new features
- Add inline code comments
- Write clear function docstrings
- Update API documentation

### 🐛 Bug Reports

Found a bug? Please create an issue with:

1. **Clear title** describing the problem
2. **Steps to reproduce** the issue
3. **Expected vs actual behavior**
4. **System information** (OS, Python version, etc.)
5. **Logs or error messages**

### 💡 Feature Requests

Have an idea? Create an issue with:

1. **Clear description** of the feature
2. **Use case** explaining why it's needed
3. **Proposed implementation** (if you have ideas)
4. **Examples** of similar features

### 🏆 Recognition

Contributors will be:
- Listed in the contributors section
- Mentioned in release notes
- Given credit in documentation
- Invited to the contributors team

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LiveKit** for real-time communication infrastructure
- **OpenAI** for advanced language model capabilities
- **Deepgram** for accurate speech recognition
- **Cartesia** for high-quality text-to-speech
- **FastAPI** for the modern web framework
- **Contributors** who make this project better

## 📞 Support

- **Documentation**: [Wiki](https://github.com/AbhiramVSA/VISU-Reborn/wiki)
- **Issues**: [GitHub Issues](https://github.com/AbhiramVSA/VISU-Reborn/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AbhiramVSA/VISU-Reborn/discussions)
- **Email**: [Support](mailto:support@visu-ai.com)

## ⭐ Show Your Support

If you find VISU helpful, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** to contribute
- 📢 **Sharing** with others
- 💝 **Sponsoring** the project

---

<div align="center">
  <strong>Built with ❤️ by the VISU Community</strong>
  <br>
  <em>Making AI more emotionally intelligent, one conversation at a time</em>
</div>
