from flask_restful import Resource
from flask import render_template
from ..core.services import IncomingMessageHelper
from app import api
from ..common import SOCKET_IO_API, output_html


@api.route(SOCKET_IO_API)
class IncomingSocketMessage(Resource):
    def get(self):
        return output_html(render_template('index.html'), 200)

    def post(self):
        IncomingMessageHelper()


