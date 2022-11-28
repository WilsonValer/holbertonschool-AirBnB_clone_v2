#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, String
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""
        def __init__(self, *args, **kwargs):
            """initializes state"""
            super().__init__(*args, **kwargs)

        @property
        def cities(self):
            """ property that returs a list of city instances
            """
            city_list = []
            all_cities = models.storage.all(City).values()
            for city in all_cities:
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
