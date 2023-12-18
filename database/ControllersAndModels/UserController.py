import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.User import User

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

  

    def insert_user(self, name):
            session = self.Session()
            user = User(name=name)
            session.add(user)
            session.commit()
            session.close()

    def delete_user(self, user_id):
        session = self.Session()
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def update_user(self, user_id, new_name):
        session = self.Session()
        user = session.query(User).get(user_id)
        if user:
            user.name = new_name
            session.commit()
        session.close()
    
    def get_user_recipes(self, user_id: int):
        session = self.Session()
        user = session.query(User).get(user_id)
        if user:
            return user.recipes
        return []


if __name__ == "__main__":
    # Create an instance of UserController
    user_controller = UserController()
    user_controller.insert_user("connor Holley")