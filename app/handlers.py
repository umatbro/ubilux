from asyncio import sleep

from sanic.log import logger

from app.redis_utils import redis_connect

STATUS_KEY = 'status'


async def switch_status(request, ws):
    r = redis_connect()

    while True:
        logger.info('Listening for status change...')
        set_status = await ws.recv()

        logger.info(f'Received status: {set_status}, sending status to redis')
        r.set(STATUS_KEY, set_status)


async def subscribe_to_switch_status(request, ws):
    r = redis_connect()

    if not r.exists(STATUS_KEY):
        logger.info('Setting initial status value to 0')
        r.set(STATUS_KEY, '0')
    status = r.get(STATUS_KEY).decode('utf-8')

    # send current status
    logger.info(f'Sending initial status: {status}')
    await ws.send(status)

    p = r.pubsub()
    p.psubscribe(f'__keyspace@*__:{STATUS_KEY}')

    while True:
        message = p.get_message()
        await sleep(0.001)

        if message is None:
            continue

        logger.info(message)
        data = message.get('data')

        if data == b'set':
            new_status = r.get(STATUS_KEY).decode('utf-8')
            logger.info(f'Received new status: {new_status}')
            await ws.send(new_status)
        else:
            logger.error(f'Unexpected message data: {data}')
