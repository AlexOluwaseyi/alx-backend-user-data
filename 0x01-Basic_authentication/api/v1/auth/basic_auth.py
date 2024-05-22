#!/usr/bin/env python3

"""Authorization module
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic authentication
    Inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the
        Authorization header for a Basics
        Authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        auth_type, auth_cred = authorization_header.split()
        return auth_cred
