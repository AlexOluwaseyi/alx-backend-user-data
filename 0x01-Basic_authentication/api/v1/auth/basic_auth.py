#!/usr/bin/env python3

"""Authorization module
"""

from flask import request
from typing import List, TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication 
    Inherits from Auth
    """
    pass
