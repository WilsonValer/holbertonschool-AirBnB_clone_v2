"""
module for the DBSstorage
"""

from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, host, database, pool_pre_ping=True))

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session (self.__session) all
            objects depending of the class name (argument cls)
        """
        class_dict = {}
        if cls is None:
            cls = [State, City, Amenity, Place, Review, User]
        else:
            cls = [cls]
        for elem in cls:
            datas = self.__session.query(elem).all()
            for result in datas:
                key = "{}.{}".format(type(result).__name__, result.id)
                class_dict[key] = result
        return class_dict
                
