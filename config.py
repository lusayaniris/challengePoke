import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sarasa_secret_key'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'sarasa_jwt_secret_key'
    TOKEN_EXPIRY_MINUTES = os.environ.get('TOKEN_EXPIRY_MINUTES') or 60

# For production, we should set environment variables for SECRET_KEY and JWT_SECRET_KEY
