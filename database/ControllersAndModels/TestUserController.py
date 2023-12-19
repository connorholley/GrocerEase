import unittest
from unittest.mock import MagicMock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import User, Recipe
from UserController import UserController

class TestUserController(unittest.TestCase):

    def setUp(self):

        self.controller = UserController(environment='testing')
        self.session= self.controller.Session()
    def tearDown(self):
        # Delete data in table after each test
        self.session.query(User).delete()
        self.session.query(Recipe).delete()
        self.session.commit()
       

    def test_insert_user(self):
        # Test inserting a user with a recipe
        recipe = Recipe(name='Test Recipe')
        self.controller.insert_user(name='Test User', recipe=recipe)

        # Check if the user and recipe were added to the database
        with self.session as session:
            user = session.query(User).filter_by(name='Test User').first()
            print(user.recipes[0])
            self.assertIsNotNone(user)
            self.assertEqual(user.recipes, [recipe])

    def test_delete_user(self):
        # Test deleting a user
        with self.session as session:
            user = User(name='Test User')
            session.add(user)
            session.commit()

            # Call delete_user method
            self.controller.delete_user(user.id)

            # Check if the user was deleted from the database
            deleted_user = session.query(User).filter_by(id=user.id).first()
            self.assertIsNone(deleted_user)

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
