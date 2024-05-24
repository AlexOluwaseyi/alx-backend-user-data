#!/usr/bin/env python3
""""User session storage model
"""

from models.base import Base


class UserSession(Base):
    """UserSession model
    Inherits from Base model
    """
    def __init__(self, *args: list, **kwargs: dict):
        """Initializer
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
