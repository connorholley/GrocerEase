import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from Models import User, Base, Recipe
from UserController import UserController

# Define a declarative base for testing
TestBase = Base

# SQLAlchemy engine for testing
engine = create_engine('sqlite:///:memory:')

# Set metadata bind and create tables in the in-memory SQLite database
TestBase.metadata.bind = engine

# Print the table names to verify creation
inspector = inspect(engine)
print("Tables in the test insert user function (after binding):", inspector.get_table_names())

TestBase.metadata.create_all(engine)

# Session for testing
Session = sessionmaker(bind=engine)

@pytest.fixture
def db_session(request):
    # Setup: clear the database at the beginning of each test
    session = Session()
    TestBase.metadata.drop_all(engine)  # Drop tables to clear the database
    TestBase.metadata.create_all(engine)  # Recreate tables
    yield session  # This is where the test runs
    # Teardown: rollback the transaction and close the session
    session.rollback()
    session.close()

@pytest.fixture
def user_controller(db_session):
    # Use the in-memory SQLite database session for the UserController
    controller = UserController()
    controller.Session = db_session
    return controller


def test_insert_user(user_controller, db_session):


    # Test the insert_user method and verify the inserted user
    user_name = "TestUser"
    user_controller.insert_user(user_name)

    # Retrieve the user from the database using the db_session fixture
    inserted_user = db_session.query(User).filter_by(name=user_name).first()

    # Assert that the user is not None (i.e., found in the database)
    assert inserted_user is not None

    # Assert the user's properties
    assert inserted_user.name == user_name


def test_delete_user(user_controller, db_session):
    # Test the delete_user method and verify the user is deleted
    user_name = "TestUser"
    user_controller.insert_user(user_name)

    # Retrieve the user from the database using the db_session fixture
    inserted_user = db_session.query(User).filter_by(name=user_name).first()

    

    # Ensure the user is not None (i.e., found in the database)
    assert inserted_user is not None

    # Test deleting the user
    user_controller.delete_user(inserted_user.id)

    # Verify the user is not found in the database after deletion
    deleted_user = db_session.query(User).filter_by(name=user_name).first()
   
    assert deleted_user is None


def test_update_user_name(user_controller, db_session):
    # Test the update_user_name method and verify the updated user name
    user_name = "TestUser"
    new_name = "UpdatedUser"
    user_controller.insert_user(user_name)

    # Retrieve the user from the database using the db_session fixture
    inserted_user = db_session.query(User).filter_by(name=user_name).first()

    # Ensure the user is not None (i.e., found in the database)
    assert inserted_user is not None

    # Test updating the user name
    user_controller.update_user_name(inserted_user.id, new_name)

    # Verify the user's name is updated in the database
    updated_user = db_session.query(User).filter_by(id=inserted_user.id).first()
    assert updated_user.name == new_name


def test_get_user_by_id(user_controller, db_session):
    # Test the get_user_by_id method and verify the retrieved user
    user_name = "TestUser"
    user_controller.insert_user(user_name)

    # Retrieve the user from the database using the db_session fixture
    inserted_user = db_session.query(User).filter_by(name=user_name).first()

    # Ensure the user is not None (i.e., found in the database)
    assert inserted_user is not None

    # Test getting the user by ID
    retrieved_user = user_controller.get_user_by_id(inserted_user.id)

    # Verify the retrieved user matches the inserted user
    assert retrieved_user.id == inserted_user.id
    assert retrieved_user.name == inserted_user.name


def test_get_user_recipes_by_id(user_controller, db_session):
    # Test the get_user_recipes_by_id method and verify the retrieved recipes
    user_name = "TestUser"
    user_controller.insert_user(user_name)

    # Retrieve the user from the database using the db_session fixture
    inserted_user = db_session.query(User).filter_by(name=user_name).first()

    # Ensure the user is not None (i.e., found in the database)
    assert inserted_user is not None

    # Test getting the user's recipes by ID
    recipes = user_controller.get_user_recipes_by_id(inserted_user.id)

    # Verify the recipes are initially empty
    assert len(recipes) == 0

    # Add a recipe to the user and test again
    new_recipe = Recipe(name="TestRecipe", description="TestDescription")
    db_session.add(new_recipe)
    db_session.commit()

    user_controller.add_recipe_to_user(new_recipe, inserted_user.id)

    # Retrieve the updated recipes and verify the added recipe is present
    updated_recipes = user_controller.get_user_recipes_by_id(inserted_user.id)
    assert len(updated_recipes) == 1
    assert updated_recipes[0].id == new_recipe.id


def test_add_recipe_to_user(user_controller, db_session):
    # Test the add_recipe_to_user method and verify the added recipe
    user_name = "TestUser"
    user_controller.insert_user(user_name)

    # Retrieve the user from the database using the db_session fixture
    inserted_user = db_session.query(User).filter_by(name=user_name).first()

    # Ensure the user is not None (i.e., found in the database)
    assert inserted_user is not None

    # Test adding a recipe to the user
    new_recipe = Recipe(name="TestRecipe", description="TestDescription")
    user_controller.add_recipe_to_user(new_recipe, inserted_user.id)

    # Retrieve the updated recipes and verify the added recipe is present
    updated_recipes = user_controller.get_user_recipes_by_id(inserted_user.id)
    assert len(updated_recipes) == 1
    assert updated_recipes[0].id == new_recipe.id


def test_remove_recipe_from_user(user_controller, db_session):
    # Test the remove_recipe_from_user method and verify the removed recipe
    user_name = "TestUser"
    user_controller.insert_user(user_name)

    # Retrieve the user from the database using the db_session fixture
    inserted_user = db_session.query(User).filter_by(name=user_name).first()

    # Ensure the user is not None (i.e., found in the database)
    assert inserted_user is not None

    # Add a recipe to the user
    new_recipe = Recipe(name="TestRecipe", description="TestDescription")
    db_session.add(new_recipe)
    db_session.commit()

    user_controller.add_recipe_to_user(new_recipe, inserted_user.id)

    # Test removing the recipe from the user
    user_controller.remove_recipe_from_user(new_recipe.id, inserted_user.id)

    # Retrieve the updated recipes and verify the removed recipe is not present
    updated_recipes = user_controller.get_user_recipes_by_id(inserted_user.id)
    assert len(updated_recipes) == 0