#!/usr/bin/python3
'''This is a module'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        '''
        An init function
        '''
        db = os.getenv('HBNB_MYSQL_DB')
        user = os.getenv('HBNB_MYSQL_USER')
        host = os.getenv('HBNB_MYSQL_HOST')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        dialect = 'mysql'
        driver = 'mysqldb'
        self.__engine = create_engine(
                f'{dialect}+{driver}://{user}:{passwd}@{host}/{db}',
                pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)

        if cls=None, query all types of objects
        (User, State, City, Amenity, Place and Review)

        return dictionary.
        '''
        objects = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        if cls:
            cls_dict = {}
            cls_obj = self.__session.query(cls)

            for i in cls_obj:
                key = f'{cls.__name__}.{i.id}'
                val = i
                cls_dict[key] = val

        else:
            for cls in objects:
                cls_dict = {}
                cls_obj = self.__session.query(eval(cls))

                for i in cls_obj:
                    key = f'{cls.__name__}.{i.id}'
                    val = i
                    cls_dict[key] = val

        return cls_dict

    def new(self, obj):
        '''
        add the object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
        commit all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        delete from the current database session obj if not None
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
        create and reload a session
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
