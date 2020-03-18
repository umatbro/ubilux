import os

import pytest
import redis
from pytest_sanic.utils import TestClient
from sanic.websocket import WebSocketProtocol

from main import app as s_app


@pytest.fixture
def test_config():
    class Config:
        REDIS_HOST = os.environ.get("TEST_REDIS_HOST", "127.0.0.1")
        REDIS_PORT = os.environ.get("TEST_REDIS_PORT", "6337")
        REDIS_DB = os.environ.get("TEST_REDIS_DB", "0")

    return Config


@pytest.fixture()
def app(test_config):
    s_app.config.from_object(test_config)
    yield s_app


@pytest.fixture()
def test_cli(loop, app, sanic_client) -> TestClient:
    return loop.run_until_complete(sanic_client(app, protocol=WebSocketProtocol))


@pytest.fixture(autouse=True)
async def redis_connection(test_config):
    r = redis.Redis(
        host=test_config.REDIS_HOST,
        port=test_config.REDIS_PORT,
        db=test_config.REDIS_DB,
    )

    yield r
    r.flushdb()
