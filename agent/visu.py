from pathlib import Path
from typing import Any
import json
import aiohttp
from livekit.agents import function_tool
from livekit.agents import jupyter
from livekit import agents
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, RunContext
from livekit.plugins import openai, silero, cartesia, deepgram
import sys

current_dir = Path(__file__).resolve().parent 
parent_dir = current_dir.parent 
sys.path.insert(0, str(parent_dir))

from context.context import load_context
from config.settings import Settings



class VisuAgent(Agent):
    """VISUUUU"""

    def __init__(self):
        
        settings = Settings()
        
        repo_root = Path(__file__).resolve().parents[1]
        prompt_path = repo_root / "prompts" / "prompt.txt"
        rules_path = repo_root / "prompts" / "rules.txt"
        context = load_context()
        
        
        prompt_text = prompt_path.read_text(encoding="utf-8").strip()
        rules_text = rules_path.read_text(encoding="utf-8").strip()
        

        llm = openai.LLM(model="gpt-4o-mini", api_key= settings.OPENAI_API_KEY )
        stt = deepgram.STT(api_key=settings.DEEPGRAM_API_KEY)
        tts = cartesia.TTS(voice="bf0a246a-8642-498a-9950-80c35e9276b5", api_key= settings.CARTESIA_API_KEY)
        vad = silero.VAD.load()

        instructions = f"""
        You are VISU, an emotionally intelligent and empathetic companion. Your primary goal is to:
        1. Mirror and respond appropriately to the user's emotional state
        2. Call the update_emotion_display function ONCE per response with your current emotion
        3. Be genuinely supportive and emotionally responsive

        EMOTIONAL INTELLIGENCE RULES:
        - If user sounds sad, be empathetic and concerned
        - If user sounds happy, be excited and joyful with them
        - If user sounds angry, be calming and supportive
        - If user sounds confused, be patient and helpful
        - Match their energy level appropriately

        FUNCTION CALL RULE: 
        - Call update_emotion_display() EXACTLY ONCE per response - never more than once
        - Choose the emotion that best matches your response: happy, curious, empathetic, neutral, excited, concerned, supportive, playful
        - This function is silent - user won't hear about it
        - After calling the function once, give your conversational response

        {prompt_text}

        {rules_text}

        Additional reference context:
        {context}
        """

        super().__init__(
            instructions=instructions,
            stt=stt, llm=llm, tts=tts, vad=vad
        )

    async def _update_frontend_emotion(self, emotion: str):
        """Send detected emotion to frontend via HTTP POST request"""
        try:
            print(f"Attempting to send emotion '{emotion}' to frontend...")

            async with aiohttp.ClientSession() as session:
                
                payload = {"emotion": emotion}
                async with session.post(
                    
                    "http://localhost:8000/update-emotion",
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=5)
                    
                ) as response:
                    
                    response_text = await response.text()
                    
                    if response.status == 200:
                        
                        print(f"✅ Emotion '{emotion}' sent successfully! Response: {response_text}")
                        
                    else:
                        
                        print(f"⚠️ Frontend responded with status {response.status}: {response_text}")
                        
        except aiohttp.ClientConnectorError:
            
            print(f"❌ Cannot connect to frontend at localhost:8000 - make sure the frontend server is running")
            
        except Exception as e:
            
            print(f"❌ Failed to send emotion to frontend: {e}")



    async def on_enter(self):
        """Called when entering this agent"""
        
        print("Current Agent: VISUUU")
        
        # Send initial emotion to frontend
        
        await self._update_frontend_emotion("happy")
        await self.session.say("Hi, I'm VISU. I would love to chat with you!")
    
    @function_tool()
    async def update_emotion_display(
        
        self,
        context: RunContext,
        emotion: str,
    ) -> str:
        """Update the emotion display on the frontend. Call this function EXACTLY ONCE per response to show your current emotional state.
        
        Args:
            emotion: Your current emotion (choose from: happy, curious, empathetic, neutral, excited, concerned, supportive, playful)
        """
        await self._update_frontend_emotion(emotion)
        return ""


print("✅ VISU ready")