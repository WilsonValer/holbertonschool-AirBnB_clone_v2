#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Foreignkey

class Review(BaseModel):
    """ Review classto store review information """

    __tablename__ =  'reviews'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullible=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=True)
        user_id = Calumn(String(60) ForeignKey('users.id'), nullable=True)
    else:
        place_id = ""
        user_id = ""
        text = ""
