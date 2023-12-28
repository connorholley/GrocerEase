from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from Factories import UserFactory, IngredientFactory, IngredientCategoryFactory, RecipeFactory, PantryItemFactory
from ControllerHelperFunctions import load_config
from Models import Recipe



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

def create_objects(factory, count):
    objects = factory.create_batch(count)
    session.add_all(objects)
    session.commit()

if __name__ == "__main__":
    main("production")
