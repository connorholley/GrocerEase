import pytest
from app.main import app


@pytest.mark.asyncio
async def test_app_provides_a_health_check():

    client = app.test_client()
    response = await client.get('/')
    assert response.status_code == 200

