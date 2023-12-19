from contextlib import contextmanager

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from .models import Ingredient

class DataService:

    def __init__(self, sql_engine: Engine):
        self._engine = sql_engine
        self._session_maker = sessionmaker(bind=self._engine)

    @contextmanager
    def _get_session(self):
        
        session = sessionmaker(bind=self._engine)
        yield session
        session.close()

    def get_all_ingredients(self):

        with self._get_session() as session:
            ingredients = session.query(Ingredient).all()

        return ingredients
