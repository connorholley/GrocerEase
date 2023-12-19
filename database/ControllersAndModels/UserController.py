import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import User, Recipe

class UserController:
    '''
    Example usage:
    user_controller = UserController(environment='testing')

    # Get user recipes
    user_recipes = user_controller.get_user_recipes(user_id=1)

    # Insert a user
    user_controller.insert_user(name='John Doe', age=30)

    # Update user information (assuming the ID is 1)
    user_controller.update_user(user_id=1, new_name='New Name')

    # Delete a user (assuming the ID is 1)
    user_controller.delete_user(user_id=1)
    '''

    def __init__(self, environment='testing'):
        print ("Hello test")
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

        # If a recipe is provided, set it for the user
        if recipe:
            user.recipes.append(recipe)

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
            if new_recipe is not None and isinstance(new_recipe, Recipe):
                user.recipes = [new_recipe]
                session.commit()
            elif new_recipe is not None:
                # Raise an exception if new_recipe is not an instance of Recipe
                raise ValueError("new_recipe must be an instance of Recipe")

        session.close()


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
