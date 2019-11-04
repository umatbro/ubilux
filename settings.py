from decouple import config
from dotenv import load_dotenv

from redis import ConnectionPool, Redis

load_dotenv()


HOST = config('HOST', default='0.0.0.0')
PORT = config('PORT', default=8000, cast=int)
DEBUG = config('DEBUG', default=False, cast=bool)
ACCESS_LOG = config('ACCESS_LOG', default=False, cast=bool)
REDIS_HOST = config('REDIS_HOST', default='127.0.0.1', cast=str)
REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
REDIS_DB = config('REDIS_DB', default=0, cast=int)

REDIS_POOL = ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
)
_r = Redis(connection_pool=REDIS_POOL)
_r.ping()
_r.close()
