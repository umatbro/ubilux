import os

import pytest
import redis
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

REDIS_TEST_PORT = 6337
load_dotenv(os.path.join(BASE_DIR, '.env-test'))


@pytest.fixture(autouse=True)
def redis_connection():
    r = redis.Redis(host='127.0.0.1', port=REDIS_TEST_PORT, db=0)
    yield r
    r.flushdb()
