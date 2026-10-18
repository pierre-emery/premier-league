"""Configuration centrale : chemins et variables d'environnement.

Tous les modules passent par ici pour savoir où lire/écrire les données.
Chaque utilisateur peut définir PLPREDICT_DATA_DIR dans son .env pour
placer le cache ailleurs que dans ./data.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Racine du dépôt : src/plpredict/config.py -> remonter de deux niveaux.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_ROOT / ".env")

DATA_DIR = Path(os.environ.get("PLPREDICT_DATA_DIR") or PROJECT_ROOT / "data")
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
