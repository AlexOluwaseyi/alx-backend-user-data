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
        print(f'creating session in sesDBauth wit uid- {user_id}')
        user_session = UserSession()
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        # session_dictionary = {}
        # session_dictionary['user_id'] = user_id
        # session_dictionary['created_at'] = datetime.now()
        # self.user_id_by_session_id[session_id] = session_dictionary
        print(f'session id = {session_id}')
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
        
        if not request:
            return None
        session_id = self.session_cookie(request)
        if not session_id:
            return None
        print(dir(UserSession))
        UserSession.remove(session_id)
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]"""
        if not request:
            return

        # Get the session ID from the request cookie
        session_id = request.cookies.get('session_id')

        if not session_id:
            return  # No session ID found, nothing to destroy

        # Remove the UserSession object from the internal storage
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]

        # Delete the session ID cookie from the client
        self._delete_session_cookie(request.response)
