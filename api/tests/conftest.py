import pytest
import os
from pathlib import Path

from app.config import ServiceConfig


@pytest.fixture
def setup_environment():

    os.environ["DB_PASSWORD"] = "test_password"

    yield

    # Tear Down
    os.environ["DB_PASSWORD"] = ""

    
@pytest.fixture
def asset_path():

    return Path(__file__).parent / "assets"


@pytest.fixture
def testing_config(setup_environment, asset_path):

    test_config_filename = asset_path / "config" / "testing_config.toml"
    
    yield ServiceConfig(
        config_filename=test_config_filename
    )
