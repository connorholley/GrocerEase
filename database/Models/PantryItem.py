
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class PantryItem(Base):
    __tablename__ = 'pantry_items'

    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    unit = Column(Enum('gram', 'milliliter', name='unit_type'), nullable=False)



