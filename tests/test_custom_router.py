from app.router import Router


class App:
    def __init__(self):
        self.routes = {}

    def add_route(self, handler, route):
        self.routes[route] = handler

    def add_websocket_route(self, handler, route):
        self.routes[route] = handler


def test_addition_of_routes():
    app = App()

    def get_num_func(num):
        def wrapped():
            return num
        return wrapped

    router = Router(app)
    router.register_routes({
        '': get_num_func(1),
        'api': {
            'login': get_num_func(2),
            'logout': get_num_func(3),
        },
        'test': get_num_func(4),
    })

    assert app.routes['/']() == 1
    assert app.routes['/api/login']() == 2
    assert app.routes['/api/logout']() == 3
    assert app.routes['/test']() == 4
