import os

from decouple import config
from redis import ConnectionPool, Redis

BASE_DIR = os.path.dirname(__file__)


HOST = config("HOST", default="0.0.0.0")
PORT = config("PORT", default=8000, cast=int)
DEBUG = config("DEBUG", default=False, cast=bool)
ACCESS_LOG = config("ACCESS_LOG", default=False, cast=bool)
NUMBER_OF_WORKERS = config("NUMBER_OF_WORKERS", default=1, cast=int)
REDIS_HOST = config("REDIS_HOST", default="127.0.0.1", cast=str)
REDIS_PORT = config("REDIS_PORT", default=6379, cast=int)
REDIS_PASSWORD = config("REDIS_PASSWORD", default="", cast=str)
REDIS_DB = config("REDIS_DB", default=0, cast=int)

REDIS_POOL = ConnectionPool(
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD
)


def check_redis_connection():
    r = Redis(connection_pool=REDIS_POOL)
    r.ping()
    r.close()
    return True
