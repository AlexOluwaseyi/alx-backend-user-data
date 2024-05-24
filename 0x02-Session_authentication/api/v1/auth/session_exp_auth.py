#!/usr/bin/env python3

"""Expiry period for session
authentication
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """Class definition for
    Session Expiration"""
        
    def __init__(self):
        """Initializer"""
        super().__init__()
        self.session_duration = int(os.getenv('SESSION_DURATION', 0))
        
    def create_session(self, user_id=None):
        """Overloads create session"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = {}
        session_dictionary['user_id'] = user_id
        session_dictionary['created_at'] = datetime.now()
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overload user id for session id"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration == 0:
            return session_dict['user_id']
        if 'created_at' not in session_dict.keys():
            return None

        expiration_time = session_dict['created_at'] +\
            timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None
        return session_dict['user_id']
