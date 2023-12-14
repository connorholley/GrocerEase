from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship, declarative_base
from Relationships import UserRecipe
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    recipes = relationship('Recipe', secondary=UserRecipe, back_populates='users')
