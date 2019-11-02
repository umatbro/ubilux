async def switch_status(request, ws):
    status = False
    while True:
        print('Send status: ', status)
        await ws.send(status)

        set_status = await ws.recv()
        print('Received status: ', set_status)
        status = set_status

