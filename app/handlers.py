from sanic.log import logger


async def switch_status(request, ws):
    status = '0'
    # send current status
    logger.info(f'Sending initial status: {status}')
    await ws.send(status)

    while True:
        logger.info('Listening for status change...')
        set_status = await ws.recv()

        logger.info(f'Received status: {set_status}')
