#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
