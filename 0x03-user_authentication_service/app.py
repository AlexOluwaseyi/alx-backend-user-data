#!/usr/bin/env python3

"""
Basic Flask App
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth
from sqlalchemy.orm.exc import InvalidRequestError
from sqlalchemy.exc import NoResultFound 

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """Root route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def reg_user():
    """Register users"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is not None and password is not None:
        try:
            user = AUTH.register_user(email, password)
            return jsonify({"email": user.email, "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400
    return ('not a valid user')


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """Login a User"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is not None and password is not None:
        try:
            user_login = AUTH.valid_login(email, password)
            if user_login:
                session_id = AUTH.create_session(email)
                response = make_response(jsonify({"email": email,
                                                  "message": "logged in"}))
                response.set_cookie('session_id', session_id)
                return response
        except Exception as e:
            abort(401)
    abort(401)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout for user session"""
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if not user:
            abort(403)
        AUTH.destroy_session(user.id)
        response = make_response(redirect('/'))
        return response
    abort(403)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile():
    """User profile"""
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
    abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """Password reset token"""
    try:
        email = request.form.get('email')
        if not email:
            abort(403)
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except NoResultFound:
        abort(403)
    except InvalidRequestError:
        abort(403)
    except ValueError:
        abort(403)

@app.route("/reset_password", methods=['PUT'], strict_slashes=False)
def update_password():
    """Password reset token"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    if not reset_token:
        abort(403)
    AUTH.update_password(reset_token, new_password)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
