import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Recipe, Ingredient, Base
from RecipeController import RecipeController


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
def recipe_controller(db_session):
    # Use the in-memory SQLite database session for the RecipeController
    controller = RecipeController()
    controller.Session = db_session
    return controller


def test_insert_recipe(recipe_controller, db_session):
    # Given we have a test recipe and an empty database
    recipe_name = "TestRecipe"
    assert db_session.query(Recipe).count() == 0

    # When we insert the recipe
    recipe_controller.insert_recipe(recipe_name, "TestInstructions", "TestDescription")

    # Then it exists in the db
    inserted_recipe = db_session.query(Recipe).filter_by(name=recipe_name).first()
    assert inserted_recipe is not None
    assert inserted_recipe.name == recipe_name


def test_delete_recipe(recipe_controller, db_session):
    # Given we have a test recipe that is inserted into the db
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    db_session.add(recipe)
    db_session.commit()

    # When we delete the recipe
    recipe_controller.delete_recipe(recipe.id)

    # Then it is removed from the database
    deleted_recipe = db_session.query(Recipe).filter_by(name=recipe.name).first()
    assert deleted_recipe is None


def test_update_recipe_name(recipe_controller, db_session):
    # Given we have a recipe with name "TestRecipe"
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    db_session.add(recipe)
    db_session.commit()

    # When we update the recipe with a new name
    recipe_controller.update_recipe(recipe.id, new_name="UpdatedRecipe")

    # Then the recipe with the id has the new name
    updated_recipe = db_session.query(Recipe).filter_by(id=recipe.id).first()
    assert updated_recipe.name == "UpdatedRecipe"

def test_update_recipe_instructions(recipe_controller, db_session):
    # Given we have a recipe with name "TestRecipe"
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    db_session.add(recipe)
    db_session.commit()

    # When we update the recipe with new instructions
    recipe_controller.update_recipe(recipe.id,new_instructions="NewInstructions")

    # Then the recipe with the id has the new instructions
    updated_recipe = db_session.query(Recipe).filter_by(id=recipe.id).first()
    assert updated_recipe.instructions == "NewInstructions"

def test_update_recipe_description(recipe_controller, db_session):
    # Given we have a recipe with name "TestRecipe"
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    db_session.add(recipe)
    db_session.commit()

    # When we update the recipe with a new description
    recipe_controller.update_recipe(recipe.id,new_description="NewDescription")

    # Then the recipe with the id has the new description
    updated_recipe = db_session.query(Recipe).filter_by(id=recipe.id).first()
    assert updated_recipe.description == "NewDescription"


def test_get_recipe_by_id(recipe_controller, db_session):
    # Given we insert a recipe with a certain name
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    db_session.add(recipe)
    db_session.commit()

    # when we call the get recipe by id function
    retrieved_recipe = recipe_controller.get_recipe_by_id(recipe.id)

    # Then it gets the correct recipe
    assert retrieved_recipe.id == recipe.id
    assert retrieved_recipe.name == recipe.name


def test_get_recipe_ingredients_by_id(recipe_controller, db_session):
    # Given we have associated an ingredient with a recipe
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    ingredient = Ingredient(name="TestIngredient")
    recipe.ingredients = [ingredient]
    db_session.add(recipe)
    db_session.add(ingredient)
    db_session.commit()

    # when we call the get recipe ingredients by id function
    updated_ingredients = recipe_controller.get_recipe_ingredients_by_id(recipe.id)

    # then it returns the correct ingredient
    assert len(updated_ingredients) == 1
    assert updated_ingredients[0].id == ingredient.id


def test_add_ingredient_to_recipe(recipe_controller, db_session):
    # When we create a recipe and an ingredient
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    db_session.add(recipe)
    db_session.commit()
    new_ingredient = Ingredient(name="TestIngredient")

    # when we add the ingredient to the recipe
    recipe_controller.add_ingredient_to_recipe(new_ingredient, recipe.id)

    # then the ingredient is associated with the recipe
    updated_ingredients = recipe_controller.get_recipe_ingredients_by_id(recipe.id)
    assert len(updated_ingredients) == 1
    assert updated_ingredients[0].id == new_ingredient.id


def test_remove_ingredient_from_recipe(recipe_controller, db_session):
    # Given we have associated an ingredient with a recipe
    recipe = Recipe(name="TestRecipe", instructions="TestInstructions", description="TestDescription")
    ingredient = Ingredient(name="TestIngredient")
    recipe.ingredients = [ingredient]
    db_session.add(recipe)
    db_session.add(ingredient)
    db_session.commit()

    # when we remove the ingredient from the recipe
    recipe_controller.remove_ingredient_from_recipe(ingredient.id, recipe.id)

    # then it gets removed
    updated_ingredients = recipe_controller.get_recipe_ingredients_by_id(recipe.id)
    assert len(updated_ingredients) == 0
