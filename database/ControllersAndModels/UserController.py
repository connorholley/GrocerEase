import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import User, Recipe

class UserController:

    def __init__(self, environment='testing'):
        self.config = self.load_config(environment)
        self.engine = create_engine(self.config['db_uri'])
        Session = sessionmaker(bind=self.engine)
        self.Session = Session()

    def load_config(self, environment):
        with open('database-config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data.get(environment, {'db_uri': 'sqlite:///:memory:'})
    
    def insert_user(self, name):
        try:
            user = User(name=name)
            self.Session.add(user)
            self.Session.commit()
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred: {e}")


    def delete_user(self, user_id):
        session = self.Session
        user= session.get(User, user_id)
        print("In user controller "+ user.name)
        try:

            if user:
                session.delete(user)
                session.commit()
              
        except Exception as e:
            session.rollback()  # Rollback the transaction in case of an exception
            print(f"An error occurred: {e}")
        


    def update_user_name(self, user_id, new_name=None):
        session = self.Session
        user = session.get(User, user_id)
        if user and new_name is not None:
            user.name = new_name
        session.commit()
        session.close()

    
    def get_user_by_id(self, user_id):
        session = self.Session
        user = session.get(User, user_id)
        return user
       
    
    def get_user_recipes_by_id(self, user_id: int):
        session = self.Session
        user= session.get(User, user_id)
        if user:
            return user.recipes
        return []
    
    def add_recipe_to_user(self, new_recipe,  user_id):
        session = self.Session
        user = session.get(User, user_id)

        if new_recipe is not None and isinstance(new_recipe, Recipe):
            if user.recipes and (new_recipe not in user.recipes) :
                user.recipes.append(new_recipe)
            else:
                # If user.recipes is empty, create a new list with new_recipe
                user.recipes = [new_recipe]
        elif new_recipe is not None:
                # Raise an exception if new_recipe is not an instance of Recipe
            raise ValueError("new_recipe must be an instance of Recipe")
    
    def remove_recipe_from_user(self, recipe_id, user_id):
            session = self.Session

            # Assuming User and Recipe are your SQLAlchemy models
            user = session.query(User).get(user_id)

            if user:
            # Use a list comprehension to filter out the recipe with the specified ID
                user.recipes = [recipe for recipe in user.recipes if recipe.id != recipe_id]

            session.commit()
            session.close()



