#!/usr/bin/env python3

"""Password encryption with Bcrypt"""

from bcrypt import hashpw, gensalt, checkpw


def hash_password(password: str) -> bytes:
    """Encrypt password"""
    hashed = hashpw(password.encode('utf-8'), gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate password"""
    hashed = hashpw(password.encode('utf-8'), gensalt())
    if checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False