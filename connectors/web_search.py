def search_web(query):
    """
    Interface de recherche Web pour Agent 1.

    Cette fonction sera connectée au moteur Web
    lorsque l'environnement compatible avec
    OpenAI Agents SDK sera utilisé.
    """

    return {
        "query": query,
        "status": "not_connected",
        "results": []
    }
