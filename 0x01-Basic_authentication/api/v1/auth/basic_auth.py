#!/usr/bin/env python3

"""Authorization module
"""

from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64
import binascii


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Returns the decoded value fo a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_b64 = base64.b64decode(base64_authorization_header)
            return decoded_b64.decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Returns the user email and password from
        Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user_email, user_pwd = decoded_base64_authorization_header.split(":")
        return user_email, user_pwd

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on
        email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for user by email
        try:
            user_list = User.search({'email': user_email})
            if not user_list or len(user_list) == 0:
                return None
        except KeyError:
            return None

        # Check the password
        user = user_list[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth and retrieves the
        User instance for the request"""
        authorization = self.authorization_header(request)
        auth_cred = self.extract_base64_authorization_header(authorization)
        decoded_b64 = self.decode_base64_authorization_header(auth_cred)
        user_email, user_pwd = self.extract_user_credentials(decoded_b64)
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
