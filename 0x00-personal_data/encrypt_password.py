#!/usr/bin/env python3

"""Password encryption with Bcrypt"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypt password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate password"""
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    return False
