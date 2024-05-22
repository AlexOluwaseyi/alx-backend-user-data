#!/usr/bin/env python3

"""Authorization module
"""

from flask import request
from typing import List, TypeVar
import os
# from models.user import User


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
        def strip(text_str: str) -> str:
            """Remove trailing "/" from text
            """
            if text_str[-1] == "/":
                return text_str[:-1]
            return text_str

        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        stripped_excluded_path = []
        for pattern in excluded_paths:
            stripped_excluded_path.append(strip(pattern))
            if pattern.endswith("*"):
                if strip(path).startswith(strip(pattern[:-1])):
                    return False
            elif strip(path) in stripped_excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Function definition to check
        authorization header from HTTP requests
        """
        if request is None:
            return None
        print(request.cookies.keys())
        if request.authorization:
            return request.authorization
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Function definition to return current user
        """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
