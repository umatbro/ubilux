import os
from typing import Dict, Union, Callable

from sanic import Sanic


def websocket_route(func):
    """
    Decorator to indicate that a route is a websocket route.
    """
    func._is_websocket_route = True
    return func


class Router:
    def __init__(self, app: Sanic):
        self.app = app

    def register_routes(self, routes: Dict[str, Union[str, Callable]]):
        """
        Register routes in the app.

        :param routes: dict where keys are the paths, and keys are the handlers
        """
        self._register_routes(routes)

    def _register_routes(self, routes: Dict[str, Union[str, Callable]], prefix_path: str = '/'):
        for route, handler in routes.items():
            if isinstance(handler, dict):
                self._register_routes(handler, prefix_path=os.path.join(prefix_path, route))
                continue
            is_websocket_handler = getattr(handler, '_is_websocket_route', False)
            add_route_func = self.app.add_websocket_route if is_websocket_handler else self.app.add_route
            add_route_func(handler, os.path.join(prefix_path, route))
