import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_openai_web_status():
    """
    Vérifie simplement si une clé OpenAI est disponible.

    La connexion réelle au Web Search sera activée
    dans l'environnement compatible avec OpenAI Agents SDK.
    """

    if not OPENAI_API_KEY:
        return {
            "status": "not_configured",
            "message": "OPENAI_API_KEY manquante."
        }

    return {
        "status": "configured",
        "message": "Clé OpenAI détectée."
    }
