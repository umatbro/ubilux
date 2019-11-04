from sanic.log import logger

import settings
from redis import Redis


def redis_connect() -> Redis:
    logger.info(f'Opening redis connection with {settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}')
    return Redis(connection_pool=settings.REDIS_POOL)
