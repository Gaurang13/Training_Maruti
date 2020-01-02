import datetime
import json
import os
from distutils.util import strtobool
__all__ = ['configure_app']


def configure_app(app):
    app.config['RABBIT_MQ_URL_PARAMETER'] = "amqp://guest:guest@localhost:5672/%2F"
    app.config['RABBIT_MQ_HOST_URL'] = "http://localhost:15672"
    app.config['RABBIT_MQ_USERNAME'] = "guest"
    app.config['RABBIT_MQ_PASSWORD'] = "guest"
    app.config['RMQ_EXCHANGE'] = "sample.direct"
    app.config['HOST'] = 'localhost'
    app.config['USER'] = 'root'
    app.config['PASSWORD'] = 'Mtech@12345'
    app.config['DB'] = 'inventory'

