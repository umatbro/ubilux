from redis import Redis
from sanic.log import logger

import settings


def redis_connect() -> Redis:
    from main import app

    logger.info(f'Opening redis connection with {settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}')
    return Redis(
        host=app.config.REDIS_HOST,
        port=app.config.REDIS_PORT,
        db=app.config.REDIS_DB,
    )


def check_redis_connection():
    r = redis_connect()
    r.ping()

    # keyspace events are required for listening status change.
    # Redis should be run with the following command:
    # redis-server --notify-keyspace-events K$$
    keyspace_events = r.config_get('notify-keyspace-events').get('notify-keyspace-events')
    assert '$' in keyspace_events
    assert 'K' in keyspace_events
    r.close()
    return True
