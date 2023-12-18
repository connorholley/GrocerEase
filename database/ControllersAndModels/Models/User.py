from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from Models.Relationships import user_recipe
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # recipes = relationship('Recipe', secondary=user_recipe, back_populates='users')
