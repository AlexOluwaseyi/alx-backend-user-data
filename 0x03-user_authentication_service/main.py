#!/usr/bin/env python3

"""
Create one function for each of the following tasks.
Use the requests module to query your web server for
the corresponding end-point. Use assert to validate the
responsels expected status code and payload (if any)
for each task.

- register_user(email: str, password: str) -> None
- log_in_wrong_password(email: str, password: str) -> None
- log_in(email: str, password: str) -> str
- profile_unlogged() -> None
- profile_logged(session_id: str) -> None
- log_out(session_id: str) -> None
- reset_password_token(email: str) -> str
- update_password(email: str, reset_token: str, new_password: str) -> None
"""

from auth import Auth
from user import User
from app import *
AUTH = Auth()


def register_user(email: str, password: str) -> None:
    """Assert return value for register user"""
    assert isinstance(email, str)
    assert isinstance(password, str)
    reg_user = AUTH.register_user(email, password)
    assert isinstance(reg_user, User)


def log_in_wrong_password(email: str, password: str) -> None:
    """Assert return value for login with wrong password"""
    assert isinstance(email, str)
    assert isinstance(password, str)
    login = AUTH.valid_login(email, password)
    assert login == False


def log_in(email: str, password: str) -> str:
    """Assert return for logged in session"""
    assert isinstance(email, str)
    assert isinstance(password, str)
    logged_in = AUTH.create_session(email)
    assert isinstance(logged_in, str)


def profile_unlogged() -> None:
    pass


def profile_logged(session_id: str) -> None:
    pass


def log_out(session_id: str) -> None:
    pass


def reset_password_token(email: str) -> str:
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    pass
logout

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)