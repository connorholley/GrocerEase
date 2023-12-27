from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from Factories import UserFactory, IngredientFactory, IngredientCategoryFactory, RecipeFactory, PantryItemFactory
from ControllerHelperFunctions import load_config

def main(environment="testing"):
    # Load configuration based on the environment
    config = load_config(environment)
    engine = create_engine(config['db_uri'])

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create instances using factories
    users = UserFactory.create_batch(20)
    ingredients = IngredientFactory.create_batch(20)
    ingredient_categories = IngredientCategoryFactory.create_batch(20)
    recipes = RecipeFactory.create_batch(20)
    pantry_items = PantryItemFactory.create_batch(20)

    # Linking pantry items to recipes and ingredients
    for idx, pantry_item in enumerate(pantry_items):
        pantry_item.recipe_id = recipes[idx].id  # Assign the ID of the recipe
        pantry_item.ingredient_id = ingredients[idx].id  # Assign the ID of the ingredient
        session.add(pantry_item)

    # Linking recipes to ingredients
    for idx, recipe in enumerate(recipes):
        recipe.ingredients.extend(ingredients)
        # Ensure that the instructions field is a text, not a list
        instructions_value = "Instruction 1\nInstruction 2\nInstruction 3"  # Replace with actual instructions
        insert_query = text("INSERT INTO recipes (name, instructions, description) VALUES (:name, :instructions::text, :description)")
        session.execute(insert_query, {'name': recipe.name, 'instructions': instructions_value, 'description': recipe.description})

    # Assigning category IDs to ingredients
    for ingredient in ingredients:
        ingredient.category_id = IngredientCategoryFactory().id
        session.add(ingredient)

    # Commit the changes to the database
    session.commit()

if __name__ == "__main__":
    main("production")
    # main("testing")
