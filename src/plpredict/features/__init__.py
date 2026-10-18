"""Construction des variables explicatives.

Règle d'or : une variable calculée pour un match à la date t n'utilise
QUE des informations disponibles strictement avant t. Les tests de
tests/test_no_leakage.py vérifient cette propriété.
"""
