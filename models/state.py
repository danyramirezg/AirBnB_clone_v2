#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete",
                              backref="my_state")
    else:
        name = ""

    if os.environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            new_list = []
            my_cities = models.storage.all(City)
            for key, value in my_cities.items():
                if value.state_id == self.id:
                    new_list.append(value)
            return new_list
