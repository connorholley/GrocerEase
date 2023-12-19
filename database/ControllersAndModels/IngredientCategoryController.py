# ingredient_category_controller.py
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import IngredientCategory

class IngredientCategoryController:
    '''
    Example usage:
    ingredient_category_controller = IngredientCategoryController(environment='testing')

    # Insert an ingredient category
    ingredient_category_controller.insert_ingredient_category(name='Grains')

    # Get all ingredient categories
    all_categories = ingredient_category_controller.get_all_ingredient_categories()
    print("All Ingredient Categories:")
    for category in all_categories:
        print(f"ID: {category.id}, Name: {category.name}")

    # Update an ingredient category (assuming the ID is 1)
    ingredient_category_controller.update_ingredient_category(category_id=1, new_name='Cereals')

    # Delete an ingredient category (assuming the ID is 1)
    ingredient_category_controller.delete_ingredient_category(category_id=1)
    '''

    # def __init__(self, environment='testing'):
    #     self.config = self.load_config(environment)
    #     self.engine = create_engine(self.config['db_uri'])
    #     IngredientCategory.metadata.create_all(self.engine)
    #     self.Session = sessionmaker(bind=self.engine)

    # def load_config(self, environment):
    #     with open('database-config.json', 'r') as config_file:
    #         config_data = json.load(config_file)
    #         return config_data.get(environment, {})

    # def insert_ingredient_category(self, name):
    #     session = self.Session()
    #     category = IngredientCategory(name=name)
    #     session.add(category)
    #     session.commit()
    #     session.close()

    # def get_all_ingredient_categories(self):
    #     session = self.Session()
    #     categories = session.query(IngredientCategory).all()
    #     session.close()
    #     return categories

    # def delete_ingredient_category(self, category_id):
    #     session = self.Session()
    #     category = session.query(IngredientCategory).get(category_id)
    #     if category:
    #         session.delete(category)
    #         session.commit()
    #     session.close()

    # def update_ingredient_category(self, category_id, new_name):
    #     session = self.Session()
    #     category = session.query(IngredientCategory).get(category_id)
    #     if category:
    #         category.name = new_name
    #         session.commit()
    #     session.close()
