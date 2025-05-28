# Architecture

## Vue d’ensemble

OrlVoice repose sur trois piliers :

1. **Speech-to-Text** : API Google Speech Recognizer
2. **NLP** : Modèle CamemBERT entraîné pour classer les intentions
3. **Vision par ordinateur** : Modèle YOLO/TFLite pour la détection visuelle

## Diagramme (exemple)

```mermaid
graph TD
  A[Voix utilisateur] --> B[Transcription STT]
  B --> C[NLP - Intent Detection]
  C --> D[Vision (si nécessaire)]
  C --> E[Action Handler]
  E --> F[Exécution sur PC/Android]
