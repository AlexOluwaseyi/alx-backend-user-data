#!/usr/bin/env python3

"""
User model module
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    The model will have the following attributes:

    id, the integer primary key
    email, a non-nullable string
    hashed_password, a non-nullable string
    session_id, a nullable string
    reset_token, a nullable string
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, *args: list, **kwargs: dict):
        """Initializer
        """
        self.email = kwargs.get('email')
        self.hashed_password = kwargs.get('hashed_password')
        self.session_id = kwargs.get('session_id')
        self.reset_token = kwargs.get('reset_token')
