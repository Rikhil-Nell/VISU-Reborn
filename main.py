from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, jupyter
from livekit import agents

from agent.visu import VisuAgent

from dotenv import load_dotenv
from config.settings import Settings

load_dotenv()

settings = Settings()

print(settings.OPENAI_API_KEY)

async def agent_entrypoint(ctx: JobContext):
    """Simple multi-agent entry point"""
    await ctx.connect()

    # Create session
    session = AgentSession()

    # Start with sales agent
    await session.start(
        agent=VisuAgent(),
        room=ctx.room
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=agent_entrypoint))
