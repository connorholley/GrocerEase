
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from Models.Relationships import ingredient_category_ingredient


Base = declarative_base()

class IngredientCategory(Base):
    __tablename__ = 'ingredient_categorys'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Many-to-Many relationship
    ingredients = relationship('Ingredient', secondary=ingredient_category_ingredient, back_populates='categories')

