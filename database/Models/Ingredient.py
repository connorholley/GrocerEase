from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from Relationships import RecipeIngredient, IngredientCategoryIngredient

Base = declarative_base()

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Ingredient and ingredient category many to many relationship
    categories = relationship('IngredientCategory', secondary=IngredientCategoryIngredient, back_populates='ingredients')

    # Ingredient and recipe many to many relationship
    recipes = relationship('Recipe', secondary=RecipeIngredient, back_populates='ingredients')


