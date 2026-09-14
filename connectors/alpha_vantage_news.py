import os
import httpx
from dotenv import load_dotenv

from .models import NewsItem

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"


USD_KEYWORDS = {
    "usd",
    "u.s. dollar",
    "us dollar",
    "american dollar",
    "federal reserve",
    "fed",
    "fomc",
    "us economy",
    "u.s. economy",
    "us inflation",
    "u.s. inflation",
    "us employment",
    "u.s. employment",
    "nonfarm payrolls",
    "treasury yields",
    "us interest rates",
}


CAD_KEYWORDS = {
    "cad",
    "canadian dollar",
    "canada dollar",
    "bank of canada",
    "boc",
    "canadian economy",
    "canadian inflation",
    "canadian employment",
    "canadian jobs",
    "canada interest rates",
    "canada gdp",
    "crude oil",
    "oil prices",
}


def is_relevant(title, summary, currencies):
    """
    Vérifie si une actualité est réellement pertinente
    pour les devises demandées.
    """

    text = f"{title} {summary}".lower()

    usd_match = any(keyword in text for keyword in USD_KEYWORDS)
    cad_match = any(keyword in text for keyword in CAD_KEYWORDS)

    if currencies == ["USD", "CAD"]:
        return usd_match or cad_match

    if currencies == ["USD"]:
        return usd_match

    if currencies == ["CAD"]:
        return cad_match

    return True


def get_news(ticker="FOREX:USD", limit=20):
    """Récupère les actualités depuis Alpha Vantage."""

    if not API_KEY:
        print("Erreur : ALPHA_VANTAGE_API_KEY manquante.")
        return []

    currencies = []

    if "/" in ticker:
        currencies = ticker.upper().split("/")

        if len(currencies) != 2:
            print("Format Forex invalide :", ticker)
            return []

        tickers = [
            f"FOREX:{currencies[0]}",
            f"FOREX:{currencies[1]}"
        ]

    else:
        tickers = [ticker.upper()]

        if ticker.upper().startswith("FOREX:"):
            currencies = [ticker.upper().replace("FOREX:", "")]

    all_news = []

    for current_ticker in tickers:
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": current_ticker,
            "limit": limit,
            "sort": "LATEST",
            "apikey": API_KEY,
        }

        try:
            response = httpx.get(
                BASE_URL,
                params=params,
                timeout=20
            )

            response.raise_for_status()
            data = response.json()

            for article in data.get("feed", []):

                title = article.get("title", "")
                summary = article.get("summary", "")

                if currencies:
                    if not is_relevant(
                        title,
                        summary,
                        currencies
                    ):
                        continue

                item = NewsItem(
                    title=title,
                    source=article.get("source", "Unknown"),
                    url=article.get("url"),
                    published_at=article.get("time_published"),
                    summary=summary,
                    sentiment=None,
                    relevance=None,
                )

                all_news.append(item)

        except Exception as error:
            print(
                f"Erreur Alpha Vantage "
                f"({current_ticker}) : {error}"
            )

    return all_news
