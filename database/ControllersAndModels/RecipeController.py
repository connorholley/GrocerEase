from .BaseController import BaseController
from sqlalchemy.orm import joinedload

from .Models import Ingredient, Recipe, RecipeIngredientRelationship

class RecipeController(BaseController):

    def __init__(self, environment='testing'):
        super().__init__(model_class=Recipe, environment=environment)


    
   
    
    # def get_ingredients_for_recipe(self, recipe_id: int):

        
    #     relationships = (
    #         self.Session.query(RecipeIngredientRelationship, Ingredient)
    #         .join(Ingredient)
    #         .filter(RecipeIngredientRelationship.recipe_id == recipe_id)
    #         .all()
    #     )

    #     return relationships
      

    def get_ingredients_for_recipe(self, recipe_id: int):
        relationships = (
            self.Session.query(RecipeIngredientRelationship, Ingredient)
            .join(Ingredient)
            .filter(RecipeIngredientRelationship.recipe_id == recipe_id)
            .all()
        )

        return [
            {
                'ingredient_id': ingredient.id,
                'name': ingredient.name,
                'amount': relationship.amount,  # Add this line to include amount
                'unit': relationship.unit      # Add this line to include unit
            }
            for relationship, ingredient in relationships
        ]


    def get_recipes_with_ingredients(self, ingredient_names: list):
        recipes_with_ingredients = (
            self.Session.query(Recipe)
            .join(RecipeIngredientRelationship)
            .join(Ingredient)
            .filter(Ingredient.name.in_(ingredient_names))
            .options(joinedload(Recipe.ingredients))
            .all()
        )

        return recipes_with_ingredients
    


    def add_ingredient_to_recipe(self, ingredient, recipe_id):
        recipe = self.get_by_id(recipe_id)

        if ingredient is not None and isinstance(ingredient, Ingredient):
            if recipe.ingredients and (ingredient not in recipe.ingredients):
                recipe.ingredients.append(ingredient)
            else:
                recipe.ingredients = [ingredient]
        elif ingredient is not None:
            raise ValueError("The ingredient parameter must be an instance of Ingredient")

    def remove_ingredient_from_recipe(self, ingredient_id, recipe_id):
        recipe = self.get_by_id(recipe_id)

        if recipe:
            recipe.ingredients = [ingredient for ingredient in recipe.ingredients if ingredient.id != ingredient_id]

        self.Session.commit()
