import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Recipe, Ingredient, RecipeIngredient, UserRecipe

class RecipeController:
    '''
    # Example usage:
        recipe_controller = RecipeController(environment='testing')

    # Insert a recipe
        recipe_controller.insert_recipe(name='Chocolate Cake', instructions=['Step 1', 'Step 2'], description='Delicious cake recipe')

    # Get all recipes
        all_recipes = recipe_controller.get_all_recipes()
        print("All Recipes:")
        for recipe in all_recipes:
            print(f"ID: {recipe.id}, Name: {recipe.name}, Instructions: {recipe.instructions}, Description: {recipe.description}")

    # Get all ingredients for a particular recipe (assuming the recipe ID is 1)
        ingredients_for_recipe = recipe_controller.get_all_ingredients_for_recipe(recipe_id=1)
        print(f"Ingredients for Recipe ID 1:")
        for ingredient in ingredients_for_recipe:
            print(f"ID: {ingredient.id}, Name: {ingredient.name}")

    # Update a recipe (assuming the ID is 1)
        recipe_controller.update_recipe(recipe_id=1, description='Updated description')

    # Delete a recipe (assuming the ID is 1)
        recipe_controller.delete_recipe(recipe_id=1)
    '''
    def __init__(self, environment='testing'):
        self.config = self.load_config(environment)
        self.engine = create_engine(self.config['db_uri'])
        Recipe.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def load_config(self, environment):
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data.get(environment, {})

    def insert_recipe(self, name, instructions, description=None):
        session = self.Session()
        recipe = Recipe(name=name, instructions=instructions, description=description)
        session.add(recipe)
        session.commit()
        session.close()

    def get_all_recipes(self):
        session = self.Session()
        recipes = session.query(Recipe).all()
        session.close()
        return recipes

    def delete_recipe(self, recipe_id):
        session = self.Session()
        recipe = session.query(Recipe).get(recipe_id)
        if recipe:
            session.delete(recipe)
            session.commit()
        session.close()

    def update_recipe(self, recipe_id, description):
        session = self.Session()
        recipe = session.query(Recipe).get(recipe_id)
        if recipe:
            recipe.description = description
            session.commit()
        session.close()

    def get_all_ingredients_for_recipe(self, recipe_id):
        session = self.Session()
        recipe = session.query(Recipe).get(recipe_id)
        if recipe:
            return recipe.ingredients
        return []
