from sanic import Sanic

import settings
from app import handlers

app = Sanic()

app.add_websocket_route(handlers.switch_status, '/switch')
app.add_websocket_route(handlers.subscribe_to_switch_status, '/listen')


if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
        access_log=settings.ACCESS_LOG,
    )
