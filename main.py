from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse
from sanic.response import json
from dotenv import load_dotenv
from envparse import Env
from app import handlers

load_dotenv()
env = Env(
    HOST=dict(cast=str, default='0.0.0.0'),
    PORT=dict(cast=int, default=8000),
    DEBUG=dict(cast=bool, default=False),
    ACCESS_LOG=dict(cast=bool, default=False),
)

app = Sanic()
app.config.update(
    {key: env(key) for key in env.schema.keys()}
)


@app.route('/')
async def index(request: Request) -> HTTPResponse:
    return json({'hello': 'world'})

app.add_websocket_route(handlers.switch_status, '/switch')


if __name__ == '__main__':
    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        access_log=app.config.ACCESS_LOG,
    )
