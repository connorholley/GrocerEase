import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Ingredient

class IngredientController:
    '''
    Example usage:
    ingredient_controller = IngredientController(environment='testing')

    # Insert an ingredient
    ingredient_controller.insert_ingredient(name='Flour')

    # Get all ingredients
    all_ingredients = ingredient_controller.get_all_ingredients()
    print("All Ingredients:")
    for ingredient in all_ingredients:
        print(f"ID: {ingredient.id}, Name: {ingredient.name}")

    # Update an ingredient (assuming the ID is 1)
    ingredient_controller.update_ingredient(ingredient_id=1, new_name='Whole Wheat Flour')

    # Delete an ingredient (assuming the ID is 1)
    ingredient_controller.delete_ingredient(ingredient_id=1)
    '''

    def __init__(self, environment='testing'):
        self.config = self.load_config(environment)
        self.engine = create_engine(self.config['db_uri'])
        Ingredient.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def load_config(self, environment):
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data.get(environment, {})

    def insert_ingredient(self, name):
        session = self.Session()
        ingredient = Ingredient(name=name)
        session.add(ingredient)
        session.commit()
        session.close()

    def get_all_ingredients(self):
        session = self.Session()
        ingredients = session.query(Ingredient).all()
        session.close()
        return ingredients

    def delete_ingredient(self, ingredient_id):
        session = self.Session()
        ingredient = session.query(Ingredient).get(ingredient_id)
        if ingredient:
            session.delete(ingredient)
            session.commit()
        session.close()

    def update_ingredient(self, ingredient_id, new_name):
        session = self.Session()
        ingredient = session.query(Ingredient).get(ingredient_id)
        if ingredient:
            ingredient.name = new_name
            session.commit()
        session.close()
