from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .ControllerHelperFunctions import load_config

class BaseController:
    def __init__(self, model_class, environment):
        self.config = load_config(environment)
        self.engine = create_engine(self.config['db_uri'])
        Session = sessionmaker(bind=self.engine)
        self.Session = Session()
        self.model_class = model_class

    def create(self, name=None, **kwargs):
        try:
            if 'name' in kwargs:
                name = kwargs.pop('name')
            instance = self.model_class(name=name, **kwargs)
            self.Session.add(instance)
            self.Session.commit()
            return instance
        except Exception as e:
            self.Session.rollback()
            print(f"An error occurred: {e}")


    def delete(self, instance_id):
        session = self.Session
        instance = session.get(self.model_class, instance_id)
        try:
            if instance:
                session.delete(instance)
                session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    def update(self, instance_id, data):
        session = self.Session
        instance = session.get(self.model_class, instance_id)
        if instance and data:
            for key, value in data.items():
                setattr(instance, key, value)
            session.commit()

    def get_by_id(self, instance_id):
        session = self.Session
        return session.get(self.model_class, instance_id)
    
    def get_all(self):
        session = self.Session
        return session.query(self.model_class).all()

