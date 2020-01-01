import datetime
import json
import os
from distutils.util import strtobool

__all__ = ['configure_app']


def configure_app(app):
    app.config[
        'RABBIT_MQ_URL_PARAMETER'] = "amqp://guest:guest@localhost:5672/%2F"
    app.config['RABBIT_MQ_HOST_URL'] = "http://localhost:15672"
    app.config['RABBIT_MQ_USERNAME'] = "guest"
    app.config['RABBIT_MQ_PASSWORD'] = "guest"
    app.config['RMQ_EXCHANGE'] = "sample.direct"
    app.config['TEMPLATE_ID'] = "d-12935ce6a3a74e56a7e66d2d8fc386d5"
    app.config['API_KEY'] = "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"
