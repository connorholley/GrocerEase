from sqlalchemy import create_engine, Column, Integer, String, Text, ARRAY
from sqlalchemy.orm import relationship, declarative_base

from Models.Relationships import user_recipe, recipe_ingredient

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    instructions = Column(ARRAY(Text), nullable=False)
    description = Column(Text)

    #many to many relationships
    ingredients = relationship('Ingredient', secondary=recipe_ingredient, back_populates='recipes')
    users = relationship('User', secondary=user_recipe, back_populates='recipes')


 
