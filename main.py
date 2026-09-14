import asyncio
import sys
from agents import Runner
from agents_system import orchestrator

async def main():
    request = " ".join(sys.argv[1:]).strip() or "Analyse USD/CAD"
    result = await Runner.run(orchestrator, request)
    print("\n" + result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
