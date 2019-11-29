from sanic.testing import SanicTestClient
from sanic.websocket import WebSocketProtocol

import pytest
from main import app as s_app


@pytest.fixture()
def app():
    yield s_app


@pytest.fixture()
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app, protocol=WebSocketProtocol))


async def test_index_returns_404(test_cli: SanicTestClient):
    response = await test_cli.get('/')
    assert response.status == 404


async def test_get_status(test_cli):
    ws_listen = await test_cli.ws_connect('/listen')
    ws_switch = await test_cli.ws_connect('/switch')
    init_status = await ws_listen.receive()
    assert init_status.data == '0'
    await ws_switch.send_str('1')
    end_status = await ws_listen.receive()
    assert end_status.data == '1'
