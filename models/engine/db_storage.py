#!/usr/bin/python3
""" DATABASE storage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine import URL
from models.base_model import Base
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
import os


class DBStorage:
    """ Database Engine """

    __engine = None
    __session = None

    def __init__(self):
        _url = URL.create(
                "mysql+mysqldb", os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"), os.getenv("HBNB_MYSQL_HOST"),
                3306, os.getenv("HBNB_MYSQL_DB")
                )

        self.__engine = create_engine(_url, pool_pre_ping=True)
        if (os.getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ return a specific cls or all classes """

        objects = None
        _classes = [Amenity, User, State, City, Place, Review]
        if (cls is not None):
            objects = self.__session.query(cls)
        else:
            objects = []
            for cls in _classes:
                objects.append(self.__session.query(cls))

        return {'{}.{}'.format(type(obj).__name__, obj.id):
                obj for obj in objects}

    def reload(self):
        """ create all Tables """

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
                sessionmaker(self.__engine, expire_on_commit=False)
                )
        self.__session = Session()

    def new(self, obj):
        """ add new object """
        if (obj in self.__Session):
            self.__session.merge(obj)
        else:
            self.__session.add(obj)
            self.__session.commit()

    def delete(self, obj=None):
        """ delet obj if its there """
        if (obj is None and obj in self.__session):
            self.__session.delete(obj)

    def save(self):
        """ commit the changes to the session """
        self.__session.commit()

    def close(self):
        """ close the session """
        self.__session.close()
