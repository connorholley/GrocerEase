
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from Relationships import IngredientCategoryIngredient


Base = declarative_base()

class IngredientCategory(Base):
    __tablename__ = 'ingredient_categorys'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Many-to-Many relationship
    ingredients = relationship('Ingredient', secondary=IngredientCategoryIngredient, back_populates='categories')
