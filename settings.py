import os

from decouple import config

BASE_DIR = os.path.dirname(__file__)


HOST = config('HOST', default='0.0.0.0')
PORT = config('PORT', default=8000, cast=int)
DEBUG = config('DEBUG', default=False, cast=bool)
ACCESS_LOG = config('ACCESS_LOG', default=False, cast=bool)
REDIS_HOST = config('REDIS_HOST', default='127.0.0.1', cast=str)
REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
REDIS_DB = config('REDIS_DB', default=0, cast=int)
