#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan",
                            backref="state", passive_deletes=True)
    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id"""          
            list_cities = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    list_cities.append(city)
            return list_cities