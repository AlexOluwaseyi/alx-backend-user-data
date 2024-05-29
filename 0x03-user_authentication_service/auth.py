#!/usr/bin/env python3

"""
User authentication module
"""

import bcrypt
from bcrypt import gensalt
from db import DB
from typing import TypeVar
from user import User
from sqlalchemy.orm.exc import NoResultFound
import pytest


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes DB storage
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """take mandatory email and password string
        arguments and return a User object.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {user.email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user


def _hash_password(password: str) -> bytes:
    """method that takes in a password string
    arguments and returns bytes.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), gensalt())
    return hashed_password