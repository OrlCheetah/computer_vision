# Fonctionnalités

## ✅ Fonctionnalités actuelles

# Fonctionnalités d'OrlVoice

OrlVoice est une application innovante de commande vocale qui interprète les intentions de l'utilisateur grâce à un modèle de **traitement du langage naturel (NLP)**. Voici les principales fonctionnalités qu'elle prend en charge :

---

## 🧠 Compréhension des commandes vocales

Le modèle NLP est entraîné pour **reconnaître et classifier automatiquement** un ensemble de commandes vocales permettant de piloter l'ordinateur. Ci-dessous, les types d'actions comprises :

### 🎯 Catégories d'actions

#### 1. **Commandes de mouvement de la souris**

Ces commandes permettent de déplacer le curseur dans une direction spécifique d’un nombre de pixels donné :

```
deplacer_souris:[direction]_[distance]
```

* Exemple : `deplacer_souris:haut_50`, `deplacer_souris:gauche_150`

**Directions supportées** :

* `haut`, `bas`, `gauche`, `droite`

---

#### 2. **Actions de clic**

Commandes simulant les clics de souris :

* `clic gauche`
* `clic droit`
* `double clic`

---

#### 3. **Défilement (scroll)**

Commandes pour faire défiler l'écran dans une direction :

* `scroll haut`
* `scroll bas`
* `scroll gauche`
* `scroll droite`

---

#### 4. **Saisie de texte**

Commande pour écrire dynamiquement du texte :

* `écrire_texte`

---

#### 5. **Lancement et fermeture d’applications**

* `ouvrir_app` : pour ouvrir une application (ex. : "ouvre WhatsApp")
* `fermer_app` : pour la fermer

---

### 🧾 Liste complète des commandes reconnues

les commandes de deplacement de la souris sont au format `deplacer_souris:[direction]_[distance]` où :
* `[direction]` peut être `haut`, `bas`, `gauche`, `droite` `[distance]` est un nombre de pixels qui peut [3, 5, 10, 20, 50, 100, 150, 200, 240, 300] (ex. : `deplacer_souris:haut_50` déplace la souris de 50 pixels vers le haut).

```
deplacer_souris:gauche_5
scroll gauche
déplacer souris
double clic
écrire_texte
clic gauche
scroll droite
deplacer_souris:droite_10
scroll haut
clic droit
fermer_app
scroll bas
ouvrir_app
deplacer_souris:haut_5
deplacer_souris:droite_3
deplacer_souris:gauche_200
deplacer_souris:droite_200
deplacer_souris:gauche_100
deplacer_souris:haut_240
deplacer_souris:bas_150
deplacer_souris:haut_50
deplacer_souris:droite_20
deplacer_souris:droite_50
deplacer_souris:gauche_20
deplacer_souris:bas_300
deplacer_souris:haut_100
deplacer_souris:bas_100
deplacer_souris:gauche_3
deplacer_souris:bas_5
deplacer_souris:droite_300
deplacer_souris:haut_20
deplacer_souris:bas_3
deplacer_souris:gauche_150
deplacer_souris:droite_100
deplacer_souris:droite_5
deplacer_souris:gauche_50
deplacer_souris:gauche_240
deplacer_souris:bas_240
deplacer_souris:bas_50
deplacer_souris:bas_200
deplacer_souris:gauche_300
deplacer_souris:haut_3
deplacer_souris:haut_10
deplacer_souris:haut_200
deplacer_souris:droite_240
deplacer_souris:bas_20
deplacer_souris:haut_300
deplacer_souris:bas_10
deplacer_souris:gauche_10
deplacer_souris:droite_150
deplacer_souris:haut_150
```

---

## 🔄 Fonctionnalités en développement

* 📱 Compatibilité Android (Jetpack Compose)
* 👁️ Détection d’éléments visuels à l’écran avec vision par ordinateur (YOLO)
* ❤️ Correction intelligente des fautes de transcription vocale
* 🧠 Apprentissage dynamique des chemins d’exécution pour les applications inconnues

---

OrlVoice est conçu pour évoluer rapidement. Les nouvelles fonctionnalités sont ajoutées au fur et à mesure des versions.
> 🔧 Cette application est toujours en développement actif.
