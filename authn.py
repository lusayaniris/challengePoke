from flask import jsonify, request
from datetime import timedelta
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request
)
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config import Config
import logging

# Dummy user data, replace with real database query in production
users = {
    "admin": generate_password_hash("password")
}


def authenticate_user(username, password):
    """Check if a username/password combination is valid."""
    user_password_hash = users.get(username)
    if user_password_hash and check_password_hash(user_password_hash, password):
        return True
    return False


def create_access_token_for_user(username):
    """Create a new JWT access token for the user."""
    # Token expires in 60 minutes
    return create_access_token(identity=username, expires_delta=timedelta(minutes=Config.TOKEN_EXPIRY_MINUTES))


def initialize_jwt(app):
    """Initialize JWT with Flask app."""
    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        return jsonify({"error": "Missing Authorization Header"}), 401

    return jwt


def requires_auth(f):
    """JWT required decorator."""

    @wraps(f)  # This is essential to keep the original function's name and other metadata
    @jwt_required()
    def decorated(*args, **kwargs):
        verify_jwt_in_request()  # Ensures JWT is valid
        user_identity = get_jwt_identity()  # Fetch the user's identity
        return f(*args, **kwargs)

    return decorated


def login():
    """Endpoint to log in a user and return a JWT."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if authenticate_user(username, password):
        access_token = create_access_token_for_user(username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401