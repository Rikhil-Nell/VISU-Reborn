# VISU Emotion Frontend

A simple, real-time emotion display for the VISU voice assistant agent.

## Features

- 🎭 **Real-time emotion display** - Shows current emotion from VISU agent
- 🌈 **Visual feedback** - Different colors and emojis for each emotion
- ⚡ **WebSocket connection** - Instant updates with no refresh needed
- 🎨 **Smooth animations** - Pulse effects when emotions change
- 📱 **Responsive design** - Works on desktop and mobile

## Supported Emotions

- **Happy** 😊 - Yellow/Gold
- **Curious** 🤔 - Sky Blue  
- **Empathetic** 🤗 - Purple
- **Neutral** 😐 - Light Gray
- **Excited** 🤩 - Tomato Red
- **Concerned** 😟 - Orange
- **Supportive** 🫂 - Light Green
- **Playful** 😄 - Hot Pink

## Quick Start

### Method 1: Using the startup script (Recommended)
```bash
cd frontend
python start.py
```

### Method 2: Manual setup
```bash
cd frontend
pip install -r requirements.txt
python server.py
```

## Usage

1. **Start the frontend server**:
   ```bash
   python start.py
   ```

2. **Open your browser** to http://localhost:8000

3. **Run your VISU agent** - it will automatically send emotions to the frontend

4. **Watch emotions update in real-time** as users interact with VISU

## API Endpoints

- `GET /` - Main emotion display page
- `POST /update-emotion` - Receives emotion updates from VISU agent
- `GET /health` - Health check endpoint
- `WS /ws` - WebSocket for real-time updates

## Example Agent Integration

The VISU agent sends emotions via HTTP POST:

```python
# This is already implemented in your agent
async def _update_frontend_emotion(self, emotion: str):
    async with aiohttp.ClientSession() as session:
        payload = {"emotion": emotion}
        await session.post("http://localhost:8000/update-emotion", json=payload)
```

## Troubleshooting

### Port 8000 already in use
```bash
# Kill process using port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Dependencies not installing
```bash
# Manual installation
pip install fastapi uvicorn websockets pydantic
```

### WebSocket connection fails
- Check if server is running on port 8000
- Ensure no firewall blocking localhost connections
- Try refreshing the browser page

## Development

The frontend consists of:
- `server.py` - FastAPI backend with WebSocket support
- Embedded HTML/CSS/JS - Real-time emotion display interface
- `requirements.txt` - Python dependencies
- `start.py` - Convenient startup script

## Architecture

```
VISU Agent → HTTP POST → FastAPI Server → WebSocket → Browser Display
     ↓              ↓             ↓            ↓
   emotion      /update-emotion   /ws      Real-time UI
```

The system is designed to be lightweight, reliable, and easy to extend with additional emotion visualization features.