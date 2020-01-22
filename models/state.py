#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
import models
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    """If environment variable is different to DBStorage return the list of
    City objects from storage linked to the current State """

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list.append(city)
            return list
    else:
        cities = relationship("City", backref="state", cascade="delete")
