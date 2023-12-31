from sqlalchemy import create_engine, text, insert
from sqlalchemy.orm import sessionmaker
from Factories import UserFactory, IngredientFactory, IngredientCategoryFactory, RecipeFactory, PantryItemFactory
from ControllerHelperFunctions import load_config
from Models import Recipe, User, Ingredient, IngredientCategory, recipe_ingredient_relationships, user_recipe_relationships, ingredient_category_relationships
import random


config = load_config("production")
engine = create_engine(config['db_uri'])

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


def main(environment="testing"):
    # Load configuration based on the environment

    # Create 20 instances of each model using factories
    create_objects(UserFactory, 20)
    create_objects(RecipeFactory, 20)
    create_objects(PantryItemFactory, 20)
    create_objects(IngredientCategoryFactory, 20)
    create_objects(IngredientFactory, 20)

    # Create relationships
    create_relationships(User, Recipe, user_recipe_relationships, 'user_id', 'recipe_id', 20)
    create_relationships(Recipe, Ingredient, recipe_ingredient_relationships, 'recipe_id', 'ingredient_id', 20)
    create_relationships(Ingredient, IngredientCategory, ingredient_category_relationships, 'ingredient_id',
                         'ingredient_category_id', 20)


def create_objects(factory, count, **kwargs):
    objects = factory.create_batch(count, **kwargs)
    session.add_all(objects)
    session.commit()


def create_relationships(parent_model, child_model, relationship_table, parent_column, child_column, count):
    parent_instances = session.query(parent_model).all()
    child_instances = session.query(child_model).all()

    for i in range(count):
        parent_instance = parent_instances[i]
        child_instance = child_instances[i]

        # Build an insert statement for the relationship table
        stmt_values = {parent_column: parent_instance.id, child_column: child_instance.id}

        # Check if it's a recipe_ingredient_relationships and insert amount and unit
        if relationship_table == recipe_ingredient_relationships:
            random_amount = random.uniform(0.1, 10.0)  # Adjust the range as needed
            random_unit = random.choice(['cups', 'teaspoons', 'grams', 'pieces'])  # Add more units as needed
            stmt_values.update({'amount': random_amount, 'unit': random_unit})

        stmt = insert(relationship_table).values(stmt_values)
        session.execute(stmt)

    session.commit()


if __name__ == "__main__":
    main("production")
