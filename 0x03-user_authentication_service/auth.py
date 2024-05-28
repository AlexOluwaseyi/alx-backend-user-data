#!/usr/bin/env python3

"""
User authentication module
"""

import bcrypt
from bcrypt import gensalt

def _hash_password(password: str) -> bytes:
    """method that takes in a password string
    arguments and returns bytes.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), gensalt())
    return hashed_password
