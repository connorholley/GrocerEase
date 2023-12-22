import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from Models import User, Base, Recipe
from UserController import UserController


TestBase = Base
engine = create_engine('sqlite:///:memory:')
TestBase.metadata.bind = engine
TestBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@pytest.fixture
def db_session(request):
    # Setup: clear the database at the beginning of each test
    session = Session()
    TestBase.metadata.drop_all(engine)  
    TestBase.metadata.create_all(engine)  
    yield session  
   
    session.rollback()
    session.close()

@pytest.fixture
def user_controller(db_session):
    # Use the in-memory SQLite database session for the UserController
    controller = UserController()
    controller.Session = db_session
    return controller


def test_insert_user(user_controller, db_session):
    # Given we have a test user and empty database 
    user_name = "TestUser"
    assert db_session.query(User).count() == 0

    # When we insert the user
    user_controller.insert_user(user_name)

    # Then it exists in the db
    inserted_user = db_session.query(User).filter_by(name=user_name).first()
    assert inserted_user is not None
    assert inserted_user.name == user_name


def test_delete_user(user_controller, db_session):
    # Given we have a test user that is inserted into the db
    user= User(name="Test User")
    db_session.add(user)
    db_session.commit()

    # When we delete the user
    user_controller.delete_user(user.id)

    # Then it is removed from the database
    deleted_user = db_session.query(User).filter_by(name=user.name).first()
    assert deleted_user is None


def test_update_user_name(user_controller, db_session):
    # Given we have a user with name test user 
    user= User(name="Test User")
    db_session.add(user)
    db_session.commit()

    # When we update the users name
    user_controller.update_user_name(user.id, "UpdatedUser")

    # Then the user with the id has the new name
    updated_user = db_session.query(User).filter_by(id=user.id).first()
    assert updated_user.name == "UpdatedUser"


def test_get_user_by_id(user_controller, db_session):
    # Given we insert a user with a certain name
    user= User(name="Test User")
    db_session.add(user)
    db_session.commit()

    # when we call the get user by id function
    retrieved_user = user_controller.get_user_by_id(user.id)

    # Then it gets the correct user
    assert retrieved_user.id == user.id
    assert retrieved_user.name == user.name


def test_get_user_recipes_by_id(user_controller, db_session):
    # Given we have associated a recipe with a user
    user = User(name="connor ")
    recipe = Recipe(name="spicy recipe")
    user.recipes= [recipe]
    db_session.add(recipe)
    db_session.add(user)
    db_session.commit()

    # when we call the get user recipes by id function
    updated_recipes = user_controller.get_user_recipes_by_id(user.id)

    #then it returns the correct recipe
    assert len(updated_recipes) == 1
    assert updated_recipes[0].id == recipe.id


def test_add_recipe_to_user(user_controller, db_session):
    # When we create a user and a recipe
    user= User(name="Test User")
    db_session.add(user)
    db_session.commit()
    new_recipe = Recipe(name="TestRecipe", description="TestDescription")

    # when we add the recipe to the user
    user_controller.add_recipe_to_user(new_recipe, user.id)

    # then the recipe is associated with the user
    updated_recipes = user_controller.get_user_recipes_by_id(user.id)
    assert len(updated_recipes) == 1
    assert updated_recipes[0].id == new_recipe.id


def test_remove_recipe_from_user(user_controller, db_session):
    # Given we have associated a recipe with a user
    user = User(name="connor ")
    recipe = Recipe(name="spicy recipe")
    user.recipes= [recipe]
    db_session.add(recipe)
    db_session.add(user)
    db_session.commit()


    # when we remove the recipe from the user
    user_controller.remove_recipe_from_user(recipe.id, user.id)

    # then it gets removed
    updated_recipes = user_controller.get_user_recipes_by_id(user.id)
    assert len(updated_recipes) == 0