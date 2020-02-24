from dotenv import load_dotenv
from sanic import Sanic

import settings
from app import handlers

load_dotenv('.env-test')

app = Sanic()
app.config.from_object(settings)

app.add_websocket_route(handlers.switch_status, '/switch')
app.add_websocket_route(handlers.subscribe_to_switch_status, '/listen')


if __name__ == '__main__':
    from app.redis_utils import check_redis_connection

    check_redis_connection()

    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        access_log=app.config.ACCESS_LOG,
    )
