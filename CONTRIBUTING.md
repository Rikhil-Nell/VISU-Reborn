# Contributing to VISU-Reborn

Thank you for your interest in contributing to VISU-Reborn! 🎉

This document provides guidelines and information for contributors.

## 🚀 Quick Start for Contributors

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/VISU-Reborn.git
   cd VISU-Reborn
   ```

2. **Set up Development Environment**
   ```bash
   uv sync  # or pip install -r requirements.txt
   cp .env.example .env  # Add your API keys
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🎯 Types of Contributions

### 🐛 Bug Fixes
- Fix existing issues
- Improve error handling
- Performance optimizations

### ✨ New Features
- Emotion detection improvements
- New voice capabilities
- Frontend enhancements
- Additional language support

### 📚 Documentation
- README improvements
- Code documentation
- Tutorials and guides
- API documentation

### 🧪 Testing
- Unit tests
- Integration tests
- Manual testing procedures
- Test automation

## 📋 Development Process

### Before You Start
1. Check existing issues and PRs
2. Create an issue to discuss major changes
3. Get feedback from maintainers

### Making Changes
1. **Write clean, readable code**
2. **Follow existing code style**
3. **Add tests for new features**
4. **Update documentation**
5. **Test thoroughly**

### Code Style Guidelines

#### Python Code
```python
# Use Black formatting
black .

# Follow PEP 8
# Use type hints where possible
def process_emotion(emotion: str) -> dict[str, Any]:
    """Process emotion with clear docstrings."""
    pass

# Use descriptive variable names
user_emotion_state = detect_emotion(audio_input)
```

#### Commit Messages
```bash
# Format: type(scope): description
feat(emotion): add support for surprise emotion
fix(frontend): resolve WebSocket connection issues
docs(readme): update installation instructions
test(agent): add emotion detection unit tests
```

### Testing Your Changes

#### Manual Testing
```bash
# Test the voice assistant
uv run main.py

# Test the frontend
cd frontend && python server.py
```

#### Automated Testing
```bash
# Run all tests
pytest

# Run specific test files
pytest tests/test_emotion.py
```

## 🎭 Emotion System Development

### Adding New Emotions

1. **Update emotion list** in `agent/visu.py`:
   ```python
   # Add to the emotion choices
   emotions = ["happy", "curious", "empathetic", "neutral", 
              "excited", "concerned", "supportive", "playful", "surprised"]
   ```

2. **Add frontend visualization** in `frontend/server.py`:
   ```javascript
   const emotionEmojis = {
       'surprised': '😲',
       // ... other emotions
   };
   ```

3. **Update CSS colors**:
   ```css
   .surprised { color: #FF1493; }
   ```

4. **Test the new emotion**:
   - Trigger the emotion in conversation
   - Verify frontend display
   - Check color and animation

### Emotion Detection Improvements

- Enhance sentiment analysis
- Add emotion intensity levels
- Improve context understanding
- Add emotion history tracking

## 🌐 Frontend Development

### Technologies Used
- **FastAPI** - Backend API
- **WebSockets** - Real-time communication
- **HTML/CSS/JS** - Frontend interface
- **Uvicorn** - ASGI server

### Adding Features
1. **Backend changes** in `frontend/server.py`
2. **Frontend updates** in the embedded HTML
3. **WebSocket message handling**
4. **CSS styling and animations**

### UI/UX Guidelines
- **Keep it simple** and intuitive
- **Use consistent colors** for emotions
- **Smooth animations** for transitions
- **Responsive design** for all devices

## 🔧 Agent Development

### Core Components
- **LLM Integration** - OpenAI/Cerebras
- **Speech Processing** - Deepgram STT, Cartesia TTS
- **Emotion Detection** - Function tools
- **Context Management** - Dynamic loading

### Adding New Capabilities

#### New Function Tools
```python
@function_tool()
async def your_new_tool(
    self,
    context: RunContext,
    parameter: str,
) -> str:
    """Description of what this tool does.
    
    Args:
        parameter: Description of the parameter
    """
    # Implementation
    return "Tool result"
```

#### Prompt Engineering
- Update `prompts/prompt.txt` for personality
- Update `prompts/rules.txt` for behavior
- Test with various conversation scenarios

## 🧪 Testing Guidelines

### Unit Tests
```python
import pytest
from agent.visu import VisuAgent

def test_emotion_detection():
    agent = VisuAgent()
    emotion = agent.detect_emotion("I'm feeling sad")
    assert emotion in ["empathetic", "concerned"]
```

### Integration Tests
- Test full conversation flows
- Verify emotion updates reach frontend
- Check WebSocket connections

### Manual Testing Scenarios
- **Happy conversation** - Verify excited responses
- **Sad conversation** - Check empathetic responses  
- **Confused user** - Test helpful responses
- **Angry user** - Verify calming responses

## 🐛 Bug Report Template

When reporting bugs, include:

```markdown
## Bug Description
Clear description of the issue

## Steps to Reproduce
1. Start the application
2. Say "I'm feeling sad"
3. Notice incorrect emotion display

## Expected Behavior
Should show empathetic emotion (purple, 🤗)

## Actual Behavior
Shows happy emotion (gold, 😊)

## Environment
- OS: Windows 11
- Python: 3.11.5
- VISU Version: 1.0.0

## Logs
```
[Include relevant error messages or logs]
```
```

## 💡 Feature Request Template

```markdown
## Feature Description
Clear description of the proposed feature

## Use Case
Why is this feature needed?

## Proposed Implementation
How should this feature work?

## Examples
Similar features in other applications

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

## 📝 Pull Request Guidelines

### PR Checklist
- [ ] **Descriptive title** and description
- [ ] **Tests added** for new features
- [ ] **Documentation updated**
- [ ] **Code follows style guidelines**
- [ ] **No breaking changes** (or clearly documented)
- [ ] **Linked to related issues**

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Manual testing completed
- [ ] Unit tests added/updated
- [ ] Integration tests pass

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Related Issues
Closes #123
```

## 🏆 Recognition

### Contributors Hall of Fame
Contributors are recognized in:
- README contributors section
- Release notes
- Project documentation
- Annual contributor highlights

### Contribution Levels
- **🌟 First-time contributor** - Welcome package
- **🚀 Regular contributor** - Repository collaborator access
- **🏆 Core contributor** - Maintainer privileges
- **💎 Champion** - Special recognition and badges

## 📞 Getting Help

### Community Support
- **GitHub Discussions** - General questions and ideas
- **GitHub Issues** - Bug reports and feature requests
- **Discord** - Real-time chat (coming soon)

### Maintainer Contact
- Create an issue for technical questions
- Use discussions for general questions
- Email for private concerns

## 📚 Resources

### Learning Resources
- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

### Development Tools
- **Code Editor**: VS Code with Python extension
- **Version Control**: Git with GitHub
- **Testing**: pytest framework
- **Formatting**: Black, isort, flake8

## 🎉 Thank You!

Your contributions make VISU-Reborn better for everyone. Whether you're fixing bugs, adding features, improving documentation, or helping other users, every contribution matters!

---

**Happy Contributing! 🚀**