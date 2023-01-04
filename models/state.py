#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            '''
            getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id
            '''
            import models
            city_list = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
