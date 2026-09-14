from .alpha_vantage_news import get_news
from .official_sources import get_official_sources
from .web_search import search_web
from .openai_web import get_openai_web_status
from .agent1_report import Agent1Report


def research_asset(asset):
    """
    Collecte les informations nécessaires à Agent 1.
    """

    print(f"\nRecherche Agent 1 : {asset}")

    # 1. Actualités financières
    news = get_news(asset)

    # 2. Sources officielles
    official_sources = get_official_sources()

    # 3. Recherche Web
    web_results = search_web(
        f"{asset} latest news macroeconomics geopolitics "
        f"central bank economic data"
    )

    # 4. Vérification de la configuration OpenAI
    openai_web = get_openai_web_status()

    # 5. Création du rapport
    report = Agent1Report(
        asset=asset,
        news=news,
        economic_data=[],
        central_banks=[],
        geopolitics=[],
        upcoming_events=[],
        contradictions=[],
        confirmed_information=[],
        information_to_confirm=[],
    )

    # 6. Résultat final
    return {
        "instructions": "AGENT1_INSTRUCTIONS",
        "report": report.to_dict(),
        "official_sources": official_sources,
        "web_results": web_results,
        "openai_web": openai_web,
    }
