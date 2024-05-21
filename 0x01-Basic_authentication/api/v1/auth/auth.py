#!/usr/bin/env python3

"""Authorization module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class definition for authorization methods
    """
    def __init__(self) -> None:
        """Initializers
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Function definition to check is authentication
        is required to access path/route
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Function definition to check
        authorization header from HTTP requests
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Function definition to return current user
        """
        return None
