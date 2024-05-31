#!/usr/bin/env python3

"""
User authentication module
"""

import bcrypt
from bcrypt import gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes DB storage
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
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

    def valid_login(self, email: str, password: str) -> bool:
        """
        It should expect email and password
        required arguments and return a boolean.

        Try locating the user by email. If it exists,
        check the password with bcrypt.checkpw. If it
        matches return True. In any other case, return False.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password)
            return False
        except NoResultFound:
            return False
        except InvalidRequestError:
            return False

    def create_session(self, email):
        """ It takes an email string argument
        and returns the session ID as a string.

        The method should find the user corresponding
        to the email, generate a new UUID and store it
        in the database as the user's session_id, then
        return the session ID."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user, session_id=session_id)
                return user.session_id
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None

    def get_user_from_session_id(self, session_id: str):
        """It takes a single session_id string argument
        and returns the corresponding User or None.

        If the session ID is None or no user is found,
        return None. Otherwise return the corresponding
        user."""
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None

    def destroy_session(self, user_id: int) -> None:
        """takes a single user_id integer
        argument and returns None.

        The method updates the corresponding
        user's session ID to None."""
        try:
            user = self._db.find_user_by(id=user_id)
            if user:
                user.session_id = None
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None
        return None

    def get_reset_password_token(self, email: str) -> str:
        """It take an email string argument
        and returns a string.

        Find the user corresponding to the email.
        If the user does not exist, raise a
        ValueError exception. If it exists,
        generate a UUID and update the user's
        reset_token database field. Return the token."""
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                raise ValueError
            reset_token = _generate_uuid()
            self._db.update_user(user, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None
        except Exception as e:
            return None

    def update_password(self, reset_token, password):
        """ It takes reset_token string argument and
        a password string argument and returns None.

        Use the reset_token to find the corresponding user.
        If it does not exist, raise a ValueError exception.

        Otherwise, hash the password and update the user's
        hashed_password field with the new hashed password
        and the reset_token field to None."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if not user:
                raise ValueError
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, {'password': hashed_password,
                                           'reset_token': None})
            return None
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None
        except ValueError:
            return None


def _hash_password(password: str) -> bytes:
    """method that takes in a password string
    arguments and returns bytes.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), gensalt())
    return hashed_password


def _generate_uuid() -> str:
    """Generate uuid
    and return str version"""
    return str(uuid.uuid4())
