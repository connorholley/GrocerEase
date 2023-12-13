from sqlalchemy import create_engine, Column, Integer, String, Text, ARRAY
from sqlalchemy.orm import relationship, declarative_base, Session
from Ingredient import Ingredient
from Relationships import UserRecipe, RecipeIngredient

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    instructions = Column(ARRAY(Text), nullable=False)
    description = Column(Text)

    #many to many relationships
    ingredients = relationship('Ingredient', secondary=RecipeIngredient, back_populates='recipes')
    users = relationship('User', secondary=UserRecipe, back_populates='recipes')


 
