
from .Models import User, Recipe
from .BaseController import BaseController


class UserController(BaseController):
    def __init__(self, environment='testing'):
        super().__init__(User, environment)

    def get_user_recipes_by_id(self, user_id):
        user = self.get_by_id(user_id)
        return user.recipes if user else []


    def add_recipe_to_user(self, new_recipe, user_id):
        user = self.get_by_id(user_id)

        if new_recipe and isinstance(new_recipe, Recipe):
            if user.recipes and (new_recipe not in user.recipes):
                user.recipes.append(new_recipe)
            else:
                user.recipes = [new_recipe]
        elif new_recipe:
            raise ValueError("new_recipe must be an instance of Recipe")

    def remove_recipe_from_user(self, recipe_id, user_id):
        user = self.get_by_id(user_id)

        if user:
            user.recipes = [recipe for recipe in user.recipes if recipe.id != recipe_id]

        self.Session.commit()