#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from salalchemy import Column, Integer, String, Foreignkey, Float, Table
from sqlalchemy.orm import relationhip
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))

class Place(BaseModel):
    """ A place to stay """
    __tanblename__ = 'places'
    if genenv('HBNB_TYPE_STORAGE') == 'db':
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

        reviews = relationship("Review", backref="Place",
                               cascade="all, delete, delete-orphan")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="place_amenities")
    
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

        @property
        def reviews(self):
            new_reviw_list = []
            for val in models.storage.all(Review).values():
                if val.place_id == self.id:
                    new_review_list.append(val)
                    return new_review_list
        @property
        def amenities(self):
            new_amenity_list = []
            for value in models.storage.all(Amenity).values():
                if value.place_amenity.place_id == self.id:
                    new_amenity_list.append(value)
                return new_amenity_list

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
