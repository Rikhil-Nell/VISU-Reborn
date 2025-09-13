"""
Simple FastAPI server for VISU emotion frontend
Receives emotion updates from the agent and broadcasts to connected clients
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import json
import asyncio
from datetime import datetime

app = FastAPI(title="VISU Emotion Frontend")

# Pydantic model for emotion data
class EmotionUpdate(BaseModel):
    emotion: str

# Store active WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"✅ Client connected. Total connections: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        print(f"❌ Client disconnected. Total connections: {len(self.active_connections)}")

    async def broadcast(self, message: dict):
        """Broadcast message to all connected clients"""
        if not self.active_connections:
            print("⚠️ No clients connected to broadcast emotion")
            return
            
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_text(json.dumps(message))
            except Exception as e:
                print(f"❌ Failed to send to client: {e}")
                disconnected.append(connection)
        
        # Remove disconnected clients
        for conn in disconnected:
            self.disconnect(conn)

manager = ConnectionManager()

@app.post("/update-emotion")
async def update_emotion(emotion_data: EmotionUpdate):
    """Receive emotion update from VISU agent and broadcast to clients"""
    emotion = emotion_data.emotion.lower()
    timestamp = datetime.now().isoformat()
    
    print(f"🎭 Received emotion: {emotion}")
    
    # Broadcast to all connected WebSocket clients
    message = {
        "type": "emotion_update",
        "emotion": emotion,
        "timestamp": timestamp
    }
    
    await manager.broadcast(message)
    
    return {"status": "success", "emotion": emotion, "timestamp": timestamp}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time emotion updates"""
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/")
async def get_index():
    """Serve the main HTML page"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VISU Emotion Display</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
            }
            
            .container {
                text-align: center;
                padding: 2rem;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                min-width: 400px;
            }
            
            .title {
                font-size: 2.5rem;
                margin-bottom: 1rem;
                font-weight: 300;
            }
            
            .emotion-display {
                margin: 2rem 0;
            }
            
            .emotion-text {
                font-size: 3rem;
                font-weight: bold;
                margin-bottom: 1rem;
                text-transform: capitalize;
                transition: all 0.3s ease;
            }
            
            .emotion-icon {
                font-size: 6rem;
                margin-bottom: 1rem;
                transition: all 0.3s ease;
            }
            
            .status {
                font-size: 1.2rem;
                margin-top: 2rem;
                opacity: 0.8;
            }
            
            .timestamp {
                font-size: 0.9rem;
                margin-top: 1rem;
                opacity: 0.6;
            }
            
            /* Emotion-specific styles */
            .happy { color: #FFD700; }
            .curious { color: #87CEEB; }
            .empathetic { color: #DDA0DD; }
            .neutral { color: #F0F0F0; }
            .excited { color: #FF6347; }
            .concerned { color: #FFA500; }
            .supportive { color: #98FB98; }
            .playful { color: #FF69B4; }
            
            .pulse {
                animation: pulse 1s ease-in-out;
            }
            
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1); }
            }
            
            .connected {
                color: #90EE90;
            }
            
            .disconnected {
                color: #FFB6C1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="title">VISU Emotion Display</h1>
            
            <div class="emotion-display">
                <div class="emotion-icon" id="emotionIcon">🤖</div>
                <div class="emotion-text neutral" id="emotionText">Waiting...</div>
            </div>
            
            <div class="status" id="status">Connecting to server...</div>
            <div class="timestamp" id="timestamp"></div>
        </div>

        <script>
            const emotionIcon = document.getElementById('emotionIcon');
            const emotionText = document.getElementById('emotionText');
            const status = document.getElementById('status');
            const timestamp = document.getElementById('timestamp');
            
            // Emotion to emoji mapping
            const emotionEmojis = {
                'happy': '😊',
                'curious': '🤔',
                'empathetic': '🤗',
                'neutral': '😐',
                'excited': '🤩',
                'concerned': '😟',
                'supportive': '🫂',
                'playful': '😄'
            };
            
            // WebSocket connection
            let socket;
            
            function connect() {
                socket = new WebSocket(`ws://${window.location.host}/ws`);
                
                socket.onopen = function(event) {
                    console.log('Connected to WebSocket');
                    status.textContent = 'Connected - Waiting for emotions...';
                    status.className = 'status connected';
                };
                
                socket.onmessage = function(event) {
                    const data = JSON.parse(event.data);
                    if (data.type === 'emotion_update') {
                        updateEmotion(data.emotion, data.timestamp);
                    }
                };
                
                socket.onclose = function(event) {
                    console.log('WebSocket connection closed');
                    status.textContent = 'Disconnected - Reconnecting...';
                    status.className = 'status disconnected';
                    
                    // Reconnect after 3 seconds
                    setTimeout(connect, 3000);
                };
                
                socket.onerror = function(error) {
                    console.error('WebSocket error:', error);
                    status.textContent = 'Connection error - Retrying...';
                    status.className = 'status disconnected';
                };
            }
            
            function updateEmotion(emotion, time) {
                // Update icon
                emotionIcon.textContent = emotionEmojis[emotion] || '🤖';
                emotionIcon.className = 'emotion-icon pulse';
                
                // Update text and color
                emotionText.textContent = emotion;
                emotionText.className = `emotion-text ${emotion}`;
                
                // Update status
                status.textContent = `Current emotion: ${emotion}`;
                status.className = 'status connected';
                
                // Update timestamp
                const date = new Date(time);
                timestamp.textContent = `Last update: ${date.toLocaleTimeString()}`;
                
                // Remove pulse animation after it completes
                setTimeout(() => {
                    emotionIcon.className = 'emotion-icon';
                }, 1000);
                
                console.log(`Emotion updated: ${emotion}`);
            }
            
            // Start connection
            connect();
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "active_connections": len(manager.active_connections),
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting VISU Emotion Frontend Server...")
    print("📱 Open http://localhost:8000 to view the emotion display")
    print("🔌 Agent should send emotions to http://localhost:8000/update-emotion")
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="info"
    )