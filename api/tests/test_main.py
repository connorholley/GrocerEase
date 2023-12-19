import pytest
from app.main import app

def test_app_provides_a_health_check():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_app_runs_with_test_config_and_mocked_data_service():

    raise NotImplementedError()
