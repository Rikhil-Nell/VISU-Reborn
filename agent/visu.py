from pathlib import Path
from livekit.agents import function_tool
from livekit.agents import jupyter
from livekit import agents
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions
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
        {prompt_text}

        {rules_text}

        Additional reference context:
        {context}
        """

        super().__init__(
            instructions=instructions,
            stt=stt, llm=llm, tts=tts, vad=vad
        )

    async def on_enter(self):
        """Called when entering this agent"""
        print("Current Agent: VISUUU")
        await self.session.say("Hi, I'm VISU. I would love to chat")


print("✅ VISU ready")