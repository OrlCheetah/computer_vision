import os

# Dossiers et fichiers à créer
structure = {
    "docs": {
        "index.md": "# 🗣️ OrlVoice\n\nBienvenue dans la documentation officielle du projet OrlVoice.",
        "presentation": {
            "apropos.md": "# À propos\n\nPrésentation du projet OrlVoice.",
            "fonctionnalites.md": "# Fonctionnalités\n\nListe des fonctionnalités actuelles et à venir.",
            "architecture.md": "# Architecture\n\nDiagrammes et explications de l’architecture technique."
        },
        "guide": {
            "installation.md": "# Installation\n\nInstructions pour installer OrlVoice.",
            "utilisation_pc.md": "# Utilisation sur PC\n\nComment utiliser OrlVoice sur ordinateur.",
            "utilisation_android.md": "# Utilisation sur Android\n\nFonctionnalités disponibles sur Android (en développement)."
        },
        "dev": {
            "configuration.md": "# Configuration\n\nParamétrage de l’environnement et des modèles.",
            "nlp.md": "# Modèle NLP\n\nInformations sur le modèle de traitement du langage.",
            "vision.md": "# Vision par ordinateur\n\nUtilisation de modèles comme YOLO pour la détection.",
            "simulation.md": "# Simulation d'actions\n\nSimulation de clics et de saisies clavier.",
            "nouvelles_commandes.md": "# Ajouter de nouvelles commandes\n\nÉtapes pour intégrer de nouveaux intents."
        },
        "faq.md": "# FAQ\n\nQuestions fréquentes et solutions.",
        "roadmap.md": "# Feuille de route\n\nFonctionnalités prévues dans les futures versions.",
        "credits.md": "# Crédits\n\nContributeurs et ressources externes utilisées."
    }
}


def create_structure(base_path, tree):
    for name, content in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ Structure de documentation créée avec succès dans le dossier 'docs/'")
