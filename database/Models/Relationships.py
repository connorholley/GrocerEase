from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

UserRecipe = Table(
    'user_recipe_relationship',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True)
)

RecipeIngredient = Table(
    'recipe_ingredient_relationship',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipe.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredient.id'))
)

IngredientCategoryIngredient = Table('ingredient_category_relationship', Base.metadata,
    Column('ingredient_id', Integer, ForeignKey('ingredient.id')),
    Column('category_id', Integer, ForeignKey('ingredient_category.id'))
)