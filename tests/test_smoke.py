"""Test de fumée : le package s'importe et la configuration est cohérente."""

import plpredict
from plpredict import config


def test_package_importable():
    assert plpredict.__version__


def test_data_dirs_under_data_dir():
    assert config.RAW_DIR.parent == config.DATA_DIR
    assert config.PROCESSED_DIR.parent == config.DATA_DIR
