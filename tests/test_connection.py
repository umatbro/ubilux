import asyncio

from pytest_sanic.utils import TestClient
from sanic.testing import SanicTestClient


async def test_index_returns_404(test_cli: SanicTestClient):
    response = await test_cli.get("/")
    assert response.status == 404


async def test_get_status(test_cli: TestClient):
    ws_listen = await test_cli.ws_connect("/listen")
    ws_switch = await test_cli.ws_connect("/switch")
    init_status = await ws_listen.receive()
    await ws_listen.close()
    assert init_status.data == "0"
    await ws_switch.send_str("1")
    ws_listen = await test_cli.ws_connect("/listen")
    end_status = await ws_listen.receive()
    assert end_status.data == "1"

    # reopen connection and check that state is 1
    ws_listen = await test_cli.ws_connect("/listen")
    status = await ws_listen.receive()
    assert status.data == "1"


async def test_set_status_by_endpoint(test_cli, redis_connection):
    status = redis_connection.get("status")
    assert status is None
    ws = await test_cli.ws_connect("/switch")
    await ws.send_str("1")
    await asyncio.sleep(0.2)

    new_status = redis_connection.get("status")
    assert new_status == b"1"
