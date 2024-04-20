#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, aliased
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(
            String(128), nullable=False
            )

    if (os.getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship(
                "City", backref="states", cascade="all, delete"
                )
    else:
        @property
        def cities(self):
            from models import storage
            for city in storage.all(City).values():
                if city.state_id == State.id:
                    cities.append(city)
            return cities

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


alias = aliased(State, name="state")
