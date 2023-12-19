import pytest
from unittest.mock import Mock, patch

from app.data_service import DataService
from app.data_service.models import (
    Ingredient
)

# TODO: there has to be a better way then this to test the database. Ideally we
# provide a test set of data to init the database with and tests can be run on
# that data.
#
# Need to identify how to do this though. This article might have a starting place:
# https://coderpad.io/blog/development/a-guide-to-database-unit-testing-with-pytest-and-sqlalchemy/


@pytest.fixture
def mock_engine():
    return Mock()

@pytest.fixture
def mock_session():
    return Mock()

@pytest.fixture
def mock_data_service_with_ingredient_data(mock_session):

    mock_session.query().all.return_value = [
        Ingredient(id=1, name='Flour'),
        Ingredient(id=2, name='Milk'),
        Ingredient(id=3, name='Egg')
    ]

    with patch("app.data_service.data_service.sessionmaker") as mock_sessionmaker:
        mock_sessionmaker.return_value = mock_session

        # Creating DataService object with the mocked engine & a patched sessionmaker 
        data_service = DataService(mock_engine)

        yield data_service

        
def test_data_service_provides_ingredient_list(mock_data_service_with_ingredient_data:DataService):
    
    ingredients = mock_data_service_with_ingredient_data.get_all_ingredients()

    for ingredient in ingredients:
        assert isinstance(ingredient, Ingredient)
