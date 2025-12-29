# 📊 Application de Statistique Descriptive Multi-Sources

### Interface graphique Tkinter avec éditeur de code intégré

---

## 📌 Présentation du projet

Ce projet consiste en une **application Python de statistique descriptive** dotée d’une **interface graphique Tkinter**, capable d’analyser des données issues de **sources multiples** (Excel, CSV, fichiers texte) et de **gérer tous les types de variables statistiques**.

L’application intègre :

* une **analyse statistique automatique adaptée au type de variable**,
* une **visualisation graphique contextuelle**,
* une **fenêtre d’édition permettant de modifier manuellement le code d’analyse et de visualisation**.

Elle est conçue pour un usage **académique, pédagogique et exploratoire**, notamment dans le cadre :

* de mémoires et rapports scientifiques,
* d’analyses d’enquêtes socio-économiques,
* de formations en statistique appliquée.

---

## 🎯 Objectifs

* Fournir un **outil d’analyse statistique rigoureux et reproductible**
* Respecter la **typologie statistique des variables** (quantitatives / qualitatives)
* Faciliter l’**exploration méthodologique** sans programmation avancée
* Offrir un **cadre expérimental sécurisé** pour tester des analyses personnalisées

---

## 🧠 Fonctionnalités principales

### 📂 Chargement des données

* Formats pris en charge :

  * `.xlsx`, `.xls` (Excel)
  * `.csv`
  * `.txt`, `.dat` (séparateur configurable)
* Chargement dynamique via interface graphique

### 🔎 Détection automatique du type de variable

* Quantitative continue
* Quantitative discrète
* Qualitative nominale / ordinale

### 📈 Analyses statistiques adaptées

* Variables quantitatives :

  * moyenne, médiane, mode
  * variance, écart-type
  * minimum, maximum
  * test de normalité (Shapiro–Wilk)
* Variables qualitatives :

  * effectifs
  * fréquences (%)
  * mode

### 📊 Visualisations graphiques

* Histogrammes (quantitatives)
* Diagrammes en barres (qualitatives)

### ✍️ Éditeur de code intégré

* Fenêtre dédiée pour :

  * modifier les analyses statistiques
  * personnaliser les graphiques
* Accès direct aux objets :

  * `data` (DataFrame pandas)
  * `variable` (Série analysée)
* Exécution dynamique du code modifié

---

## 🏗️ Architecture du projet

```
statistique-descriptive-tkinter/
│
├── statapp.py               # Application principale
├── README.md                # Documentation du projet
├── requirements.txt         # Dépendances Python
└── data/                    # (optionnel) Données d'exemple
```

---

## 🧩 Architecture logicielle

Le projet repose sur une **séparation claire des responsabilités** :

* `DataLoader`
  → Chargement multi-sources des données
* `TypeVariable`
  → Détection du type statistique
* `AnalyseStatistique`
  → Analyses descriptives adaptées
* `FenetreEditionCode`
  → Modification manuelle des analyses
* `ApplicationStatistique`
  → Interface graphique principale

Cette organisation respecte les principes **SOLID** et facilite les extensions futures.

---

## ⚙️ Installation

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/Franckcoul/statistique-descriptive-tkinter.git
cd statistique-descriptive-tkinter
```

### 2️⃣ Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### Dépendances principales

* `pandas`
* `numpy`
* `scipy`
* `matplotlib`
* `tkinter` (inclus par défaut avec Python)

---

## ▶️ Lancement de l’application

```bash
python statapp.py
```

---

## 📚 Cas d’utilisation

* Analyse de données d’enquête (producteurs, ménages, acteurs ruraux)
* Exploration statistique avant modélisation
* Appui méthodologique pour mémoires et thèses
* Outil pédagogique en statistique descriptive
* Laboratoire d’expérimentation statistique

---

## ⚠️ Limites actuelles

* Analyses uniquement **univariées**
* Pas encore de tests d’association (χ², ANOVA, corrélation)
* L’éditeur de code n’est pas sandboxé (usage académique recommandé)

---

## 🔮 Évolutions prévues

* Analyses bivariées et multivariées
* Tests conditionnels (χ², ANOVA, Kruskal-Wallis)
* Export automatique des résultats (Excel / PDF)
* Historique et traçabilité des modifications de code
* Version pédagogique guidée (templates statistiques)

---

## 📜 Licence

Ce projet est distribué sous licence **MIT**, autorisant l’utilisation, la modification et la redistribution à des fins académiques et professionnelles, sous réserve de mention de l’auteur.

---

## 👤 Auteur

**Franck Coulibaly**
Élève ingénieur agronome – spécialité eaux et forêts
Analyse statistique appliquée, économie rurale et gestion durable des ressources

---

## 🤝 Contribution

Les contributions sont bienvenues :

* corrections,
* améliorations méthodologiques,
* nouvelles fonctionnalités.

Merci de proposer une **pull request** accompagnée d’une description claire des modifications.
