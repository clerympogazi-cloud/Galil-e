from connectors.agent1_research import research_asset


def main():
    asset = input("Actif à rechercher : ").strip()

    result = research_asset(asset)

    report = result["report"]

    print("\n" + "=" * 60)
    print("AGENT 1 — RAPPORT DE RECHERCHE")
    print("=" * 60)

    print(f"\nActif : {report['asset']}")

    print("\nSources officielles disponibles :")

    for key, source in result["official_sources"].items():
        print(
            f"- {source['name']} "
            f"({source['country']})"
        )

    print("\nActualités récupérées :")

    if report["news"]:
        for news in report["news"][:10]:

            if hasattr(news, "title"):
                print(f"- {news.title}")
                print(f"  Source : {news.source}")
                print(f"  Date : {news.published_at}")
                print(f"  URL : {news.url}")

            else:
                print(f"- {news}")

    else:
        print("Aucune actualité récupérée.")

    print("\nRecherche Web :")
    print(result["web_results"])


if __name__ == "__main__":
    main()
