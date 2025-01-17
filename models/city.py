#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = sqlalchemy.Column(sqlalchemy.String(60), sqlalchemy.ForeignKey("states.id", nullable=False))
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)