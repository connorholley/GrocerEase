import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import User, Recipe

class UserController:

    def __init__(self, environment='testing'):

        self.config = self.load_config(environment)
        self.engine = create_engine(self.config['db_uri'])
        self.Session = sessionmaker(bind=self.engine)

    def load_config(self, environment):
        with open('database-config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data.get(environment, {})

  

    def insert_user(self, name, recipe=None):
        session = self.Session()
        user = User(name=name)

      
        self.add_recipe(recipe, session, user)

        session.add(user)
        session.commit()
        session.close()


    def delete_user(self, user_id):
        session = self.Session()
        user= session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def update_user(self, user_id, new_name=None, new_recipe=None):
        session = self.Session()
        user = session.get(User, user_id)

        if user:
            # Update the name if new_name is provided
            if new_name is not None:
                user.name = new_name

            # Update the recipe if new_recipe is provided and is an instance of Recipe
            self.add_recipe(new_recipe, session, user)

        session.close()

    def add_recipe(self, new_recipe, session, user):
        if new_recipe is not None and isinstance(new_recipe, Recipe):
            if user.recipes:
                    # If user.recipes already has elements, add new_recipe to the existing list
                user.recipes.append(new_recipe)
            else:
                    # If user.recipes is empty, create a new list with new_recipe
                user.recipes = [new_recipe]
            session.commit()

        elif new_recipe is not None:
                # Raise an exception if new_recipe is not an instance of Recipe
            raise ValueError("new_recipe must be an instance of Recipe")


    def show_all_users(self, ):
        session = self.Session()
        users = session.query(User).all()
      
        for user in users:
            print(user.id, user.name)
        session.close()
       
    
    def get_user_recipes(self, user_id: int):
        session = self.Session()
        user= session.get(User, user_id)
        if user:
            return user.recipes
        return []


if __name__ == "__main__":
    # Create an instance of UserController
    user_controller = UserController()

    # recipe= Recipe(name="chicken sandwhich", instructions=["hello fucker"], description="please go fuck yourself" )
    
    # user_controller.update_user(1,"logan hot boy Holley",recipe)
    # user_controller.delete_user(2)
    # recipes=user_controller.get_user_recipes(1)
    # for recipe in recipes:
    #     print(recipe.id, recipe.name, recipe.description, recipe.instructions)
    # users= user_controller.show_all_users()
