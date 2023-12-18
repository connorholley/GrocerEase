from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from Models.Relationships import recipe_ingredient, ingredient_category_ingredient

Base = declarative_base()

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Ingredient and ingredient category many to many relationship
    categories = relationship('IngredientCategory', secondary=ingredient_category_ingredient, back_populates='ingredients')

    # Ingredient and recipe many to many relationship
    recipes = relationship('Recipe', secondary=recipe_ingredient, back_populates='ingredients')


