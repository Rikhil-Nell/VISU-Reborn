#!/usr/bin/env python3
"""
Quick start script for VISU Emotion Frontend
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing frontend dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def start_server():
    """Start the FastAPI server"""
    print("🚀 Starting VISU Emotion Frontend...")
    print("📱 Open http://localhost:8000 to view the emotion display")
    print("🔌 VISU agent will send emotions to http://localhost:8000/update-emotion")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.run([sys.executable, "server.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    # Change to frontend directory
    frontend_dir = Path(__file__).parent
    os.chdir(frontend_dir)
    
    print("🎭 VISU Emotion Frontend Startup")
    print("=" * 40)
    
    # Install dependencies if needed
    if not install_dependencies():
        print("❌ Cannot start without dependencies. Please install manually:")
        print("   pip install -r requirements.txt")
        return
    
    print()
    start_server()

if __name__ == "__main__":
    main()