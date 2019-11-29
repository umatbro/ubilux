from dotenv import load_dotenv

import pytest
import redis

REDIS_TEST_PORT = 6337
load_dotenv('.env-test')


@pytest.fixture(autouse=True)
def clean_redis():
    yield
    r = redis.Redis(host='127.0.0.1', port=REDIS_TEST_PORT, db=0)
    r.flushdb()
