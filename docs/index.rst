OrlVoice
========

**OrlVoice** est une application multiplateforme de commande vocale capable d'exécuter des actions sur un PC grâce à la reconnaissance vocale, au traitement du langage naturel (NLP) et à la vision par ordinateur (computer vision). Elle fonctionne en **mode hors ligne** et permet notamment :

- d'ouvrir des applications,
- de simuler des clics,
- d’écrire du texte,
- et d’interagir dynamiquement avec une interface.

Cette application constitue un composant de notre **projet d'intelligence artificielle basé sur la vision par ordinateur**. Son objectif est de faciliter l'interaction entre le PC et l'utilisateur. **OrlVoice** sera intégrée dans un système plus large.

Fonctionnalités principales
---------------------------

- 🎤 **Activation du microphone** pour capturer les commandes vocales.
- 🧠 **Analyse des phrases** via un modèle NLP entraîné pour détecter l’intention (ex. : ``ouvre WhatsApp``, ``clique sur la loupe``, ``écris bonjour``).
- 🧭 **Correction des erreurs de transcription** (ex. : ``watsaap`` ➝ ``WhatsApp``).
- 🧾 **Apprentissage dynamique des chemins** des applications inconnues.
- 👁️ **Détection des éléments visibles à l’écran** via un modèle de vision (YOLO/TFLite). *(Fonctionnalité en développement)*
- 🖱️ **Simulation de clics** sur les coordonnées détectées par le modèle.
- 📱 **Compatibilité Android** (Jetpack Compose) et Desktop (JavaFX). *(Fonctionnalité en développement)*

Technologies utilisées
----------------------

- **NLP** : modèle CamemBERT pour la classification des commandes entrantes.
- **Vision par ordinateur** : YOLO entraîné sur des captures d’écran annotées (RICO, WhatsApp, etc.). *(Modèle non inclus)*
- **Kotlin / Jetpack Compose** : pour l’interface Android. *(Bientôt)*

Fonctionnement
--------------

#. **Commande vocale** : L'utilisateur parle, le micro capture l'audio.
#. **Transcription** : L’audio est converti en texte via l’**API Google Speech Recognizer**.
#. **Compréhension** : Le texte est analysé par un modèle NLP pour prédire l’action à exécuter.
#. **Correction (optionnelle)** : Si l’application n’est pas trouvée, l’utilisateur fournit un chemin pour l’enregistrer.
#. **Exécution** :

   - Si c’est un clic ou du texte : simulation de clic ou de saisie à l’endroit correspondant.
   - Si c’est une ouverture ou fermeture d’application : l’exécutable est lancé ou arrêté.

Installation et lancement (PC)
------------------------------

.. code-block:: bash

    git clone https://github.com/OrlCheetah/computer_vision.git
    cd computer_vision
    py
