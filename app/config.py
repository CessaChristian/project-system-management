import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
    JSON_SORT_KEYS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    AUTO_SEED = False


class DevConfig(BaseConfig):
    DEBUG = True
    AUTO_SEED = True
