#!/usr/bin/env python3

"""DB AUthentication class
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """DB Auth Class
    Inherits from SessionExpAuth"""
    def create_session(self, user_id=None):
        """Overloads create_session"""
        user_session = UserSession()
        return user_session.session_id

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
        if not session_id:
            return None
        UserSession.remove(session_id)
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
