import types

from flask import got_request_exception
from flask_socketio import SocketIO
from app.common import api_route, log_exception
from app.manage import create_app, init_task, create_api

__all__ = ["app", "api", "socketio"]

app = create_app()
api = create_api(app)
api.route = types.MethodType(api_route, api)
got_request_exception.connect(log_exception, app)
socketio = SocketIO(app)
init_task()

from app.apis import *
