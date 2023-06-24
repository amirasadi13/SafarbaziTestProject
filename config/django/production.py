import os
from .base import *  # noqa

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default=[])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = os.getenv('CORS_ORIGIN_WHITELIST', default=[])
