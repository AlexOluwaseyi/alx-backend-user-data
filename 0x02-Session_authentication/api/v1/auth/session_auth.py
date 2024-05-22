#!/usr/bin/env python3

"""Session authentication
module
"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class for
    Session Authorization
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """return user Id based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Overloads and returns a User instance
        based on a cookie value
        """
        session_name = self.session_cookie(request)
        session_id = self.user_id_for_session_id(session_name)
        user = User.get(session_id)
        return user
