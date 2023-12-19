import pytest
from app.config import ServiceConfig

def test_create_config_class(testing_config):

    assert testing_config.db_host == "localhost:4321"
    assert testing_config.db_user == "ernie"
    assert testing_config.db_password_key == "DB_PASSWORD"
    assert testing_config.db_password == "test_password"

    
def test_config_class_requires_all_values(asset_path):

    missing_value_config_filepath = asset_path / "config" / "missing_host_config.toml"

    with pytest.raises(ValueError):
        config = ServiceConfig(
            config_filename=missing_value_config_filepath
        )
