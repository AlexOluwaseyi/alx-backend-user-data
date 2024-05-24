#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.auth.session_auth import SessionAuth
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """API view to collect login info
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    user_json = user.to_json()
    response = jsonify(user_json)
    session_name = os.getenv('SESSION_NAME', '_my_session_id')
    response.set_cookie(session_name, session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """Deletes users session / logout
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        return False, abort(404)
    return jsonify({}), 200
