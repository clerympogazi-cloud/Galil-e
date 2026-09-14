# Trader Agents V2

Multi-agent research system. The user gives an asset (Forex pair, metal, index, stock, crypto, etc.).
The orchestrator identifies the asset class and assigns specialized research to four agents.

Agents:
1. Researcher — asset-specific web research.
2. Macro Analyst — fundamental interpretation.
3. Market Comparator — fundamentals vs available price/chart data.
4. Trader Presenter — final briefing and scenarios.

Examples:
python main.py "Analyse USD/CAD"
python main.py "Analyse XAU/USD"
python main.py "Analyse AAPL"

Setup:
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt

Set OPENAI_API_KEY in the environment, then:
python main.py "Analyse USD/CAD"

V2 improves the first prototype with automatic asset-class profiles and a workflow where
the user only needs to name the asset. Real market-data/chart connectors still need to be
added before this is a complete live-market platform. The system does not place trades.
