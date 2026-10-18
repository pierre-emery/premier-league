# Premier League Predictor

Prédire l'issue (victoire domicile / nul / victoire extérieur) de chaque match de Premier League,
en comparant deux familles de modèles :

- **Modèles bayésiens** (MCMC avec PyMC) : Dixon-Coles, version hiérarchique, puis force des
  équipes variable dans le temps.
- **Modèles ML** : XGBoost, CatBoost et Random Forest sur des variables construites à partir de
  l'historique des matchs.

L'objectif principal est de produire des **probabilités bien calibrées**. Le marché des paris sert
de référence à battre, et un backtest de paris sert de test de robustesse final.

Ce projet est aussi un exercice d'apprentissage : il couvre tout le pipeline de science des
données, de l'acquisition au déploiement, et chaque choix d'implémentation est documenté.

## Feuille de route

| Milestone | Contenu | Statut |
|---|---|---|
| 1. Données et EDA | Clients de téléchargement avec cache, réconciliation des sources, analyse exploratoire | En cours |
| 2. Modélisation | Références (marché, Elo), modèles bayésiens, modèles ML, validation walk-forward, backtest | À venir |
| 3. Production (optionnel) | API de prédiction (FastAPI + Docker), tableau de bord Streamlit | À venir |

Chaque milestone donne lieu à un article dans `blog/`.

## Sources de données

| Source | Contenu | Accès |
|---|---|---|
| [football-data.co.uk](https://www.football-data.co.uk/) | Résultats, statistiques de match, cotes de plusieurs bookmakers | CSV gratuits |
| [Understat](https://understat.com/) | Buts attendus (xG), depuis 2014-15 | Scraping via `soccerdata` |
| [ClubElo](http://clubelo.com/) | Classement Elo historique des clubs | Via `soccerdata` |

Périmètre : Premier League (plus Championship pour les équipes promues), à partir de 2014-15.
La dernière saison complète est réservée comme **ensemble de test** et n'est évaluée qu'une fois,
à la toute fin.

## Structure du dépôt

```
premier-league-predictor/
├── pyproject.toml          # dépendances + configuration des outils
├── uv.lock                 # versions exactes figées (généré par uv)
├── .env.example            # variables d'environnement attendues (sans valeurs)
├── .pre-commit-config.yaml # vérifications automatiques avant chaque commit
├── src/plpredict/          # le package : toute la logique réutilisable
│   ├── config.py           # chemins et variables d'environnement
│   ├── data/               # téléchargement + cache
│   ├── features/           # construction des variables (testée contre les fuites)
│   ├── models/             # bayésiens et ML, interface commune
│   └── evaluation/         # métriques, calibration, backtest
├── tests/                  # tests unitaires, dont les tests anti-fuite
├── notebooks/              # exploration, numérotés : 01_eda.ipynb, ...
├── scripts/                # entraînements lancés en ligne de commande (suivis dans W&B)
├── blog/                   # site Quarto, un article par milestone
└── data/                   # jamais commité
    ├── raw/                # téléchargements bruts, tels quels
    └── processed/          # tables nettoyées (Parquet)
```

**Principe :** les notebooks explorent et visualisent, mais ils *importent* le package.
Une fonction utile à deux notebooks va dans `src/plpredict/`.

## Installation

Le projet utilise [uv](https://docs.astral.sh/uv/) pour gérer Python et les dépendances.

```bash
# 1. Installer uv (une seule fois)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Cloner le dépôt puis créer l'environnement (installe aussi le package en mode éditable)
git clone <url-du-depot>
cd premier-league-predictor
uv sync

# 3. Configurer les variables d'environnement
cp .env.example .env        # puis remplir les valeurs

# 4. Activer les vérifications avant commit
uv run pre-commit install

# 5. Vérifier que tout fonctionne
uv run pytest
```

Pour utiliser l'environnement dans Jupyter :

```bash
uv run python -m ipykernel install --user --name=plpredict
uv run jupyter lab
```

## Bonnes pratiques du projet

- **Les données ne vont jamais dans git.** Elles sont téléchargées une fois, mises en cache dans
  `data/`, puis relues localement. Le hook `check-added-large-files` bloque les commits accidentels.
- **Les secrets restent dans `.env`**, jamais dans le code.
- **Pas de fuite temporelle.** Une variable pour un match à la date *t* n'utilise que des matchs
  antérieurs à *t*. Les tests de `tests/test_no_leakage.py` le vérifient.
- **Validation temporelle uniquement** (walk-forward), jamais de validation croisée aléatoire.
- **Chaque modèle présenté est traçable** dans Weights & Biases (configuration, métriques, artefact).
- **Les notebooks sont commités sans leurs sorties** (`nbstripout`), pour des diffs lisibles.

## Blog

```bash
quarto preview blog     # aperçu local
quarto render blog      # génère le site dans blog/_site/
```

[Quarto](https://quarto.org/) s'installe séparément (ce n'est pas un package Python).
