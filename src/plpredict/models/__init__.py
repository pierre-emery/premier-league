"""Modèles de prédiction derrière une interface commune.

Chaque modèle expose fit(...) et predict_proba(...) qui renvoie les
probabilités (victoire domicile, nul, victoire extérieur). Cette
interface commune permet de comparer bayésiens et ML avec le même
code d'évaluation.
"""
