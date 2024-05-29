#!/usr/bin/env python3

"""
Basic Flask App
"""

from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
