#!/usr/bin/env python3

"""DB AUthentication class
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """DB Auth Class
    Inherits from SessionExpAuth"""
    def __init__(self):
        super().__init__()

    def create_session(self, user_id=None):
        """Overloads create_session"""
        user_session = UserSession()
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overloads user_id_for_session_id
        """
        if not session_id:
            return None
        session_data = self.user_id_by_session_id.get(session_id)
        if not session_data:
            return None
        return session_data.get('user_id')

    def destroy_session(self, request=None):
        """Destroy session
        """
        if not request:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        user_sessions = UserSession.search({'session_id': session_id})
        if user_sessions is None or len(user_sessions) == 0:
            return None
        user_session = user_sessions[0]
        if not user_session:
            return None

        if user_session.user_id != user_id:
            return None

        user_session.remove()
        return True
