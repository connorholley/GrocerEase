from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipes = relationship('Recipe', secondary='user_recipe_relationships', back_populates='users')


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    instructions = Column(Text)
    description = Column(Text)

    # Many-to-many relationships
    ingredients = relationship('Ingredient', secondary='recipe_ingredient_relationships', back_populates='recipes')
    users = relationship(User, secondary='user_recipe_relationships', back_populates='recipes')


class PantryItem(Base):
    __tablename__ = 'pantry_items'

    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    unit = Column(Enum('gram', 'milliliter', name='unit_type'), nullable=False)


class IngredientCategory(Base):
    __tablename__ = 'ingredient_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Many-to-Many relationship
    ingredients = relationship('Ingredient', secondary='ingredient_category_relationships', back_populates='categories')


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Ingredient and ingredient category many-to-many relationship
    categories = relationship(IngredientCategory, secondary='ingredient_category_relationships', back_populates='ingredients')

    # Ingredient and recipe many-to-many relationship
    recipes = relationship(Recipe, secondary='recipe_ingredient_relationships', back_populates='ingredients')


# Relationship tables
user_recipe_relationships = Table(
    'user_recipe_relationships',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True)
)



recipe_ingredient_relationships = Table(
    'recipe_ingredient_relationships',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True),
    Column('amount', Float),  # Assuming amount is a floating-point number
    Column('unit', String),   # Assuming unit is a string, you can adjust the type as needed
)

ingredient_category_relationships = Table(
    'ingredient_category_relationships',
    Base.metadata,
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True),
    Column('ingredient_category_id', Integer, ForeignKey('ingredient_categories.id'), primary_key=True)
)



