from .ControllerHelperFunctions import load_config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .Models import Ingredient, Recipe

class RecipeController:

    def __init__(self, environment='testing'):
        self.config = load_config(environment)
        self.engine = create_engine(self.config['db_uri'])
        Session = sessionmaker(bind=self.engine)
        self.Session = Session()

   
    
    def insert_recipe(self, name, instructions,description):
        try:
            recipe = Recipe(name=name, instructions=instructions, description=description)
            self.Session.add(recipe)
            self.Session.commit()
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred: {e}")


    def delete_recipe(self, recipe_id):
        session = self.Session
        recipe= session.get(Recipe, recipe_id) 
        try:

            if recipe:
                session.delete(recipe)
                session.commit()
              
        except Exception as e:
            session.rollback()  
            print(f"An error occurred: {e}")
        


    def update_recipe(self, recipe_id, new_name=None,new_instructions=None, new_description=None):
        session = self.Session
        recipe = session.get(Recipe, recipe_id)
 
        if recipe and new_name is not None:
            recipe.name = new_name

        if recipe and new_instructions is not None:
            recipe.instructions = new_instructions
        
        if recipe and new_description is not None:
            recipe.description = new_description
        
        session.commit()
       

    
    def get_recipe_by_id(self, recipe_id):
        session = self.Session
        recipe = session.get(Recipe, recipe_id)
        return recipe
       
    
    def get_recipe_ingredients_by_id(self, recipe_id: int):
        session = self.Session
        recipe= session.get(Recipe, recipe_id)
        if recipe:
            return recipe.ingredients
        return []
    
    def add_ingredient_to_recipe(self, ingredient,  recipe_id):
        session = self.Session
        recipe = session.get(Recipe, recipe_id)

        if ingredient is not None and isinstance(ingredient, Ingredient):
            if recipe.ingredients and (ingredient not in recipe.ingredients) :
                recipe.ingredients.append(ingredient)
            else:
                recipe.ingredients = [ingredient]
        elif ingredient is not None:
                
            raise ValueError("the ingredient parameter must be an instance of Ingredient")
    
    def remove_ingredient_from_recipe(self, ingredient_id, recipe_id):
            session = self.Session

            recipe = session.query(Recipe).get(recipe_id)

            if recipe:
                recipe.ingredients = [ingredient for ingredient in recipe.ingredients if ingredient.id != ingredient_id]

            session.commit()
            



