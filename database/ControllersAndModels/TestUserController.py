import unittest
import os
import subprocess
from unittest.mock import MagicMock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import User, Recipe
from UserController import UserController

class TestUserController(unittest.TestCase):

    def setUp(self):
        #drops existing tables and creates new ones in the test db
        self.drop_and_create_test_tables()

        #instantiates a controller and a session/connection to db
        self.controller = UserController(environment='testing')
        self.session= self.controller.Session()

    def test_insert_user_succeeds(self):
        #Given we insert a user with name Test User
        self.controller.insert_user(name='Test User')

        with self.session as session:
            #When we look to validate the users presence
            user = session.query(User).filter_by(name='Test User').first()

            #Then the user Is populated with the correct name and id
            self.assertIsNotNone(user)
            self.assertEqual(user.id, 1)
            self.assertEqual(user.name, 'Test User')

    def test_insert_user_succeeds_when_recipe_is_associated(self):
        #Given we create a recipe and associate it with a user
        recipe = Recipe(name='Test Recipe')
        self.controller.insert_user(name='Test User', recipe=recipe)

       
        with self.session as session:
            #when we look to validate the users presence
            user = session.query(User).filter_by(name='Test User').first()
            recipe = session.query(Recipe).filter_by(name='Test Recipe').first()

            #then the user exists and is associated with the right recipe
            self.assertIsNotNone(user)
            self.assertEqual(user.recipes[0].id, 1)
            self.assertEqual(user.recipes[0].name, 'Test Recipe')

            #and the recipe is associated with the right user
            self.assertIsNotNone(recipe)
            self.assertEqual(recipe.users[0].id, 1)
            self.assertEqual(recipe.users[0].name, 'Test User')




    def test_delete_user_succeeds(self):
       
        with self.session as session:
            # Given we create a user
            user = User(name='Test User')
            session.add(user)
            session.commit()

            user_to_delete = session.query(User).filter_by(id=user.id).first()
            self.assertIsNotNone(user_to_delete)

            # when we call the delete method
            self.controller.delete_user(user.id)

            # Then the user is deleted
            deleted_user = session.query(User).filter_by(id=user.id).first()
            self.assertIsNone(deleted_user)


    def test_delete_user_succeeds_in_deleting_associated_users_from_recipe(self):
       
        with self.session as session:
            # Given we create a user and associate a recipe to it
            recipe = Recipe(name='Test Recipe')
            user = User(name='Test User', recipes=[recipe])
            session.add(user)
            session.commit()

            user_to_delete = session.query(User).filter_by(id=user.id).first()
            self.assertIsNotNone(user_to_delete)
            self.assertEqual(user.recipes[0].id, 1)
            self.assertEqual(user.recipes[0].name, 'Test Recipe')

            # When we call the delete method
            self.controller.delete_user(user.id)

            # Then the user is deleted from the db 
            deleted_user = session.query(User).filter_by(id=user.id).first()
            self.assertIsNone(deleted_user)

            #and the recipe is no longer associated with the user
            self.assertNotEqual(recipe.users,[user])
    
    def run_shell_script(self, script_path):
        script_dir = os.path.dirname(os.path.abspath(script_path))

        try:
            subprocess.run(["sh", script_path], check=True, cwd=script_dir)
        except subprocess.CalledProcessError as e:
            print(f"Error running {script_path} script: {e}")


    def drop_and_create_test_tables(self):
        drop_tables_script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..",  # Adjust the relative path based on your project structure
        "database/migrations/v0.0.1/drop-tables-and-set-up.sh"
    ) 
        self.run_shell_script(drop_tables_script_path)  
       

       

    # def test_update_user(self):
    #     # Test updating a user's name and adding a recipe
    #     with self.Session() as session:
    #         user = User(name='Old Name')
    #         session.add(user)
    #         session.commit()

    #         # Call update_user method
    #         new_recipe = Recipe(name='New Recipe')
    #         self.controller.update_user(user.id, new_name='New Name', new_recipe=new_recipe)

    #         # Check if the user was updated in the database
    #         updated_user = session.query(User).filter_by(id=user.id).first()
    #         self.assertIsNotNone(updated_user)
    #         self.assertEqual(updated_user.name, 'New Name')
    #         self.assertEqual(updated_user.recipes, [new_recipe])

    # def test_show_all_users(self):
    #     # Test displaying all users (this mainly checks if the method runs without errors)
    #     with self.Session() as session:
    #         user1 = User(name='User 1')
    #         user2 = User(name='User 2')
    #         session.add_all([user1, user2])
    #         session.commit()

    #         # Call show_all_users method
    #         self.controller.show_all_users()

    # def test_get_user_recipes_by_id(self):
    #     # Test getting recipes for a user
    #     with self.Session() as session:
    #         user = User(name='Test User')
    #         recipe1 = Recipe(name='Recipe 1')
    #         recipe2 = Recipe(name='Recipe 2')
    #         user.recipes = [recipe1, recipe2]
    #         session.add(user)
    #         session.commit()

    #         # Call get_user_recipes_by_id method
    #         recipes = self.controller.get_user_recipes_by_id(user.id)
    #         self.assertEqual(recipes, [recipe1, recipe2])

    # def test_add_recipe_to_user(self):
    #     # Test adding a recipe to a user
    #     with self.Session() as session:
    #         user = User(name='Test User')
    #         session.add(user)
    #         session.commit()

    #         # Call add_recipe_to_user method
    #         new_recipe = Recipe(name='New Recipe')
    #         self.controller.add_recipe_to_user(new_recipe, session, user)

    #         # Check if the recipe was added to the user in the database
    #         updated_user = session.query(User).filter_by(id=user.id).first()
    #         self.assertEqual(updated_user.recipes, [new_recipe])

    # def test_add_recipe_to_user_raises_exception(self):
    #     # Test that add_recipe_to_user raises ValueError for non-Recipe instance
    #     with self.assertRaises(ValueError):
    #         self.controller.add_recipe_to_user('Not a Recipe', MagicMock(), MagicMock())


if __name__ == '__main__':
    unittest.main()
