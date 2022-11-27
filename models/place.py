#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from salalchemy import Column, Integer, String, Foreignkey, Float, Table
from os import getenv

class Place(BaseModel):
    """ A place to stay """
    __tanblename__ = 'places'
    if genenv('HBNB_TYPE_STORAGE') == 'db'
    city_id = Column(String(60)), Foreignkey('cities.id'), nullable=false)
    user_id = Column(String(60)), Foreignkey('users.id'), nullable=false)
    name = Column(String(128), nullable=false)
    description = Column(String(1024), nullable=true)
    number_rooms = Column(integer, nullable=false, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    
else:
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
