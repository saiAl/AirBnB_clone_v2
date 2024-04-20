#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, aliased

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    email = Column(
            String(128), nullable=False
            )
    password = Column(
            String(128), nullable=False
            )
    first_name = Column(
            String(128), nullable=False
            )
    last_name = Column(
            String(128), nullable=False
            )
    places = relationship("Place", backref="users", cascade="all, delete-orphan")
    reviews = relationship("Review", backref="users", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

alias = aliased(User, name="user")
