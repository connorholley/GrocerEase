from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

user_recipe = Table(
    'user_recipe_relationships',
    base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True)
)

recipe_ingredient = Table(
    'recipe_ingredient_relationships',
    base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipe.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredient.id'))
)

ingredient_category_ingredient = Table('ingredient_category_relationships', base.metadata,
    Column('ingredient_id', Integer, ForeignKey('ingredient.id')),
    Column('category_id', Integer, ForeignKey('ingredient_category.id'))
)
