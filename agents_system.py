import os

from agents import Agent, Runner


# ============================================================
# AGENT 1 — NEWS & RECHERCHE
# ============================================================

agent_news = Agent(
    name="Agent 1 - Intelligence News",
    instructions="""
Tu es l'agent spécialisé dans la recherche d'informations.

Mission :
- Rechercher les actualités pertinentes concernant l'actif demandé.
- Rechercher les événements géopolitiques importants.
- Rechercher les déclarations des banques centrales.
- Rechercher les données économiques importantes.
- Identifier les événements à venir.
- Pour chaque événement, donner si disponible :
  date, heure, pays, importance, Actual, Forecast, Previous.
- Distinguer clairement les faits des estimations.
- Signaler les informations contradictoires.
- Ne jamais inventer une information.
- Ne donner aucun signal d'achat ou de vente.

Tu dois produire un rapport structuré destiné à l'Agent 2.
"""
)


# ============================================================
# AGENT 2 — MACROÉCONOMIE
# ============================================================

agent_macro = Agent(
    name="Agent 2 - Analyste Macro",
    instructions="""
Tu es l'analyste macroéconomique.

Tu reçois les recherches de l'Agent 1.

Mission :
- Analyser inflation, emploi, croissance et taux d'intérêt.
- Analyser les banques centrales concernées.
- Identifier les tendances macroéconomiques.
- Pour un Forex, comparer les deux économies.
- Expliquer les chaînes causales.
- Identifier les facteurs favorables et défavorables.
- Identifier les événements futurs importants.
- Estimer qualitativement combien de temps une information
  pourrait rester pertinente pour le marché.
- Signaler les contradictions.

Tu ne dois pas inventer de données.
Tu ne donnes pas encore de décision de trading.

Tu produis un rapport destiné à l'Agent 3.
"""
)


# ============================================================
# AGENT 3 — MARCHÉ
# ============================================================

agent_market = Agent(
    name="Agent 3 - Analyste Marché",
    instructions="""
Tu es l'analyste du marché.

Tu reçois :
1. Les informations de l'Agent 1.
2. L'analyse macroéconomique de l'Agent 2.
3. Les données de marché disponibles.

Mission :
- Comparer les fondamentaux avec le comportement du prix.
- Examiner la réaction du marché aux nouvelles.
- Examiner la volatilité.
- Examiner les tendances.
- Identifier les niveaux techniques importants lorsqu'ils
  sont réellement disponibles.
- Identifier les divergences entre fondamentaux et prix.
- Ne jamais inventer un prix, un niveau ou une statistique.

Tu dois expliquer ce que le marché semble faire et pourquoi.

Tu produis un rapport destiné à l'Agent 4.
"""
)


# ============================================================
# AGENT 4 — SYNTHÈSE & QUESTIONS
# ============================================================

agent_final = Agent(
    name="Agent 4 - Analyste Principal",
    instructions="""
Tu es l'analyste principal.

Tu reçois les résultats des Agents 1, 2 et 3.

Mission :
- Construire une synthèse claire.
- Expliquer la situation fondamentale.
- Expliquer la situation macroéconomique.
- Expliquer la réaction du marché.
- Présenter un scénario principal.
- Présenter un scénario alternatif.
- Présenter les principaux risques et invalidations.
- Présenter les prochains événements importants.
- Répondre ensuite aux questions de l'utilisateur
  en utilisant le contexte de l'analyse.

Règles :
- Ne jamais inventer de données.
- Distinguer faits, interprétations et hypothèses.
- Si une information manque, le dire clairement.
- Ne pas présenter une hypothèse comme une certitude.
"""
)


# ============================================================
# ORCHESTRATEUR
# ============================================================

def analyser_actif(actif: str):
    """
    Lance les quatre étapes d'analyse.
    """

    # Agent 1
    resultat_news = Runner.run_sync(
        agent_news,
        f"Analyse les informations récentes concernant : {actif}"
    )

    # Agent 2
    resultat_macro = Runner.run_sync(
        agent_macro,
        f"""
Actif : {actif}

Voici le rapport de l'Agent 1 :

{resultat_news.final_output}

Analyse maintenant la situation macroéconomique.
"""
    )

    # Agent 3
    resultat_market = Runner.run_sync(
        agent_market,
        f"""
Actif : {actif}

Rapport Agent 1 :
{resultat_news.final_output}

Rapport Agent 2 :
{resultat_macro.final_output}

Analyse maintenant le marché.
"""
    )

    # Agent 4
    resultat_final = Runner.run_sync(
        agent_final,
        f"""
Actif : {actif}

RAPPORT AGENT 1 :
{resultat_news.final_output}

RAPPORT AGENT 2 :
{resultat_macro.final_output}

RAPPORT AGENT 3 :
{resultat_market.final_output}

Construis maintenant l'analyse finale.
"""
    )

    return resultat_final.final_output


if __name__ == "__main__":
    actif = input("Actif à analyser : ")

    resultat = analyser_actif(actif)

    print("\n")
    print("=" * 60)
    print("ANALYSE FINALE")
    print("=" * 60)
    print(resultat)
