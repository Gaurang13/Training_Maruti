import os
from distutils.util import strtobool

__all__ = ['configure_app']
_AMQP_URL = 'amqp://{user_name}:{password}@{host}:{port}/%2F?heartbeat=600&retry_delay=3&connection_attempts=3&blocked_connection_timeout=300'


def configure_app(app):
    app.config['ENVIRONMENT'] = os.environ.get("ENVIRONMENT")
    app.config['DEBUG'] = strtobool(os.environ.get("DEBUG", "0"))
    app.config['TESTING'] = strtobool(os.environ.get("TESTING", "0"))
    app.config['PORT'] = int(os.environ.get("CHANNEL_SERVICE_PORT", 5015))
    app.config['SECRET_KEY'] = 'secret!'

    # Logger
    app.config['GL_SERVER'] = os.environ.get("GL_SERVER", 'localhost')
    app.config['GL_PORT'] = int(os.environ.get("GL_PORT", 12201))
    app.config['ENABLE_GRAYLOG'] = int(os.environ.get('ENABLE_GRAYLOG', 0))
