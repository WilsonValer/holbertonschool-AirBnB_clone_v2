#!/usr/bin/python3
"""
module for the DBSstorage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
#from models.amenity import Amenity
from models.city import City
from models.state import State
#from models.user import User
#from models.place import Place
#from models.review import Review
from models.base_model import BaseModel, Base


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """
        method to create instance of databse
        """
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database =getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, database), pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session) all
            objects depending of the class name (argument cls)
            if cls = None return all types of objects
        """
        class_dict = {}
        if cls is None:
            cls = [State, City]
        else:
            cls = [cls]
        for elem in cls:
            datas = self.__session.query(elem).all()
            for result in datas:
                key = "{}.{}".format(type(result).__name__, result.id)
                class_dict[key] = result
        return class_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
    

    def delete(self, obj=None):
        """delete from the current database session"""
        self.__session.delete(obj)
        self.save()

    def reload(self):
        """create all tables in the database
            sessionmaker is A factory teh produce session
            scope_session invoque to the sessionmaker
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """method to close the session"""
        self.__session.close()

