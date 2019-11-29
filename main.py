from dotenv import load_dotenv
from sanic import Sanic

from app import handlers

load_dotenv('.env-test')

app = Sanic()

app.add_websocket_route(handlers.switch_status, '/switch')
app.add_websocket_route(handlers.subscribe_to_switch_status, '/listen')


if __name__ == '__main__':

    import settings
    settings.check_redis_connection()

    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
        access_log=settings.ACCESS_LOG,
    )
