#!/usr/bin/env python3

import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Registers a new user."""
    response = requests.post(f"{BASE_URL}/users", data={"email": email, "password": password})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json() == {"email": email, "message": "user created"}, f"Unexpected response: {response.json()}"


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempts to log in with a wrong password."""
    response = requests.post(f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"


def log_in(email: str, password: str) -> str:
    """Logs in a user and returns the session ID."""
    response = requests.post(f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "session_id" in response.cookies, "Session ID not found in cookies"
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """Attempts to access profile without being logged in."""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"


def profile_logged(session_id: str) -> None:
    """Accesses profile while logged in."""
    response = requests.get(f"{BASE_URL}/profile", cookies={"session_id": session_id})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "email" in response.json(), "Email not found in response"


def log_out(session_id: str) -> None:
    """Logs out the user."""
    response = requests.delete(f"{BASE_URL}/sessions", cookies={"session_id": session_id})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def reset_password_token(email: str) -> str:
    """Gets a reset password token."""
    response = requests.post(f"{BASE_URL}/reset_password", data={"email": email})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "reset_token" in response.json(), "Reset token not found in response"
    return response.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Updates the user's password."""
    response = requests.put(f"{BASE_URL}/reset_password", data={"email": email, "reset_token": reset_token, "new_password": new_password})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json() == {"email": email, "message": "Password updated"}, f"Unexpected response: {response.json()}"


if __name__ == "__main__":
    # Example usage:
    email = "test@example.com"
    password = "Password123"

    register_user(email, password)
    log_in_wrong_password(email, "WrongPassword")
    session_id = log_in(email, password)
    profile_unlogged()
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(email)
    update_password(email, reset_token, "NewPassword123")
