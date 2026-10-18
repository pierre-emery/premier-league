"""Acquisition des données : clients de téléchargement avec cache local.

Sources prévues : football-data.co.uk (résultats, statistiques, cotes),
Understat (xG), ClubElo (classement Elo). Principe : on télécharge une
seule fois, on sauvegarde dans data/raw/, puis on relit la copie locale.
"""
