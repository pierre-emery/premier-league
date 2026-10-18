"""Tests anti-fuite de données (à compléter au milestone 2).

Idée : pour chaque variable, on modifie les matchs postérieurs à une date t
et on vérifie que les variables des matchs à la date t ne changent pas.
Si elles changent, la variable « voit le futur ».
"""

import pytest


@pytest.mark.skip(reason="Aucune variable implémentée pour l'instant.")
def test_features_do_not_use_future_matches(): ...
