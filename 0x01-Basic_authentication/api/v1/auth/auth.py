#!/usr/bin/env python3

"""Authorization module
"""

from flask import request
from typing import List, TypeVar
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
        if request.authorization:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Function definition to return current user
        """
        return None
