import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import PantryItem

class PantryItemController:
    '''
    # Example usage:
        pantry_item_controller = PantryItemController(environment='testing')

    # Insert a pantry item
        pantry_item_controller.insert_pantry_item(ingredient_id=1, amount=200, unit='gram')

    # Get all pantry items
        all_pantry_items = pantry_item_controller.get_all_pantry_items()
        print("All Pantry Items:")
        for pantry_item in all_pantry_items:
            print(f"ID: {pantry_item.id}, Ingredient ID: {pantry_item.ingredient_id}, Amount: {pantry_item.amount}, Unit: {pantry_item.unit}")

    # Update a pantry item (assuming the ID is 1)
        pantry_item_controller.update_pantry_item(pantry_item_id=1, amount=300)

    # Delete a pantry item (assuming the ID is 1)
        pantry_item_controller.delete_pantry_item(pantry_item_id=1)
    '''
    def __init__(self, environment='testing'):
        self.config = self.load_config(environment)
        self.engine = create_engine(self.config['db_uri'])
        PantryItem.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def load_config(self, environment):
        with open('database-config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data.get(environment, {})

    def insert_pantry_item(self, ingredient_id, amount, unit):
        session = self.Session()
        pantry_item = PantryItem(ingredient_id=ingredient_id, amount=amount, unit=unit)
        session.add(pantry_item)
        session.commit()
        session.close()

    def get_all_pantry_items(self):
        session = self.Session()
        pantry_items = session.query(PantryItem).all()
        session.close()
        return pantry_items

    def delete_pantry_item(self, pantry_item_id):
        session = self.Session()
        pantry_item = session.query(PantryItem).get(pantry_item_id)
        if pantry_item:
            session.delete(pantry_item)
            session.commit()
        session.close()

    def update_pantry_item(self, pantry_item_id, amount):
        session = self.Session()
        pantry_item = session.query(PantryItem).get(pantry_item_id)
        if pantry_item:
            pantry_item.amount = amount
            session.commit()
        session.close()
