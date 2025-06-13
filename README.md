# 🗣️ OrlVoice

**OrlVoice** est une application multiplateforme de commande vocale capable d'exécuter des actions sur un PC grâce à la reconnaissance vocale, au traitement du langage naturel (NLP) et à la vision par ordinateur (computer vision). Elle fonctionne en **mode online** et permet notamment d'ouvrir des applications, simuler des clics, écrire du texte et interagir dynamiquement avec une interface.

**Vous pouvez trouver notre documentation complète [ici](https://OrlCheetah.github.io/computer_vision/)**

Cette application est activement en developpement d'où certaines fonctionnalités sont encore en cours d'implémentation et des erreurs peuvent etre présentes, mais nous ttravaillons dessus.

Cette applcation constitue un composant de notre **application créée dans le cadre de notre projet d'intelligence artificielle basée sur la vision par ordinateur**. Son but est de facilier l'interacation entre PC et utilisateur. Mais bieque composant, cette application est autonome et peut être utilisée de manière autonome pour exécuter des commandes vocales sur un ordinateur.

**OrlVoice** sera intégrée dans 


## 🚀 Fonctionnalités principales

- 🎤 Activation du microphone pour capturer les commandes vocales.
- 🧠 Analyse des phrases via un modèle NLP entraîné pour détecter l’intention (ex. : "ouvre WhatsApp", "clique sur la loupe", "écris bonjour").
- 🧭 Correction des erreurs de transcription (ex : "watsaap" ➝ "WhatsApp").
- 🧾 Possibilité d'apprendre dynamiquement les chemins des applications inconnues.
- 👁️ Utilisation d’un modèle de vision (YOLO/TFLite) pour détecter les éléments visibles à l’écran. ***(Cette fonctionnfonctionnalité n'est pas encore incluse )***
- 🖱️ Simulation de clics sur les coordonnées détectées par le modèle.
- 📱 Compatible Android (Jetpack Compose) et Desktop (JavaFX). ***(Cette fonctionnfonctionnalité n'est pas encore incluse )***

---

## 🧰 Technologies utilisées

- **NLP** : modèle CammenBert pour la classification des des commandes entrantes.
- **Vision par ordinateur** : YOLO entraîné sur des screenshots annotés (RICO, WhatsApp, etc.). ***(Modèle non inclus)***
- **Kotlin / Jetpack Compose** : pour l’interface Android. ***(Bientôt)***

---

## ⚙️ Comment ça marche ?

1. **Commande vocale** : L'utilisateur parle, le micro capture l'audio.
2. **Transcription** : L'audio est converti en texte via l'**API Sppech recognizer de Google**.
3. **Compréhension** : Le texte est analysé par un modèle NLP pour prédire l'action à exécuter.
4. **Correction (optionnelle)** : Si l'application n’est pas trouvée, l’utilisateur fournit un chemin pour l'enregistrer.
5. **Exécution** :
   - Si c’est un clic ou un texte : l'application exécute l'action.
   - Une simulation de clic ou de saisie est effectuée à l’endroit correspondant.
   - Si c’est une ouverture ou fermeture d’application : l’exécutable est lancé ou fermé.
   
---

## 🖥️ Lancer l'application (PC)

```bash
git clone https://github.com/OrlCheetah/computer_vision.git
cd computer_vision
python main.py
