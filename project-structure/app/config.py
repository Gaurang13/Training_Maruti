import os
from distutils.util import strtobool

__all__ = ['configure_app']
_AMQP_URL = 'amqp://{user_name}:{password}@{host}:{port}/%2F?heartbeat=600&retry_delay=3&connection_attempts=3&blocked_connection_timeout=300'


def configure_app(app):
    app.config['ENVIRONMENT'] = os.environ.get("ENVIRONMENT")
    app.config['DEBUG'] = strtobool(os.environ.get("DEBUG", "0"))
    app.config['TESTING'] = strtobool(os.environ.get("TESTING", "0"))
    app.config['PORT'] = int(os.environ.get("CHANNEL_SERVICE_PORT", 5015))
    # MySQL
    app.config["MYSQL_DATABASE_HOST"] = os.environ.get("MYSQL_DATABASE_HOST")
    app.config["MYSQL_CORE_DATABASE"] = os.environ.get("WOTNOT_CORE_MYSQL_DATABASE")
    app.config["MYSQL_DATABASE_USER"] = os.environ.get("MYSQL_DATABASE_USER")
    app.config["MYSQL_DATABASE_PASSWORD"] = os.environ.get("MYSQL_DATABASE_PASSWORD")
    # Slack Webhook
    app.config["ERROR_WEBHOOK_URL"] = os.environ.get("ERROR_WEBHOOK_URL")
    # RabbitMQ
    app.config['RABBIT_MQ_USERNAME'] = os.environ.get('RABBIT_MQ_USERNAME')
    app.config['RABBIT_MQ_HOST_URL'] = os.environ.get('RABBIT_MQ_HOST_URL')
    app.config['RABBIT_MQ_PASSWORD'] = os.environ.get('RABBIT_MQ_PASSWORD')
    app.config['RABBIT_MQ_URL_PARAMETER'] = _AMQP_URL.format(user_name=app.config['RABBIT_MQ_USERNAME'],
                                                             password=app.config['RABBIT_MQ_PASSWORD'],
                                                             host=os.environ.get('RABBIT_MQ_HOST'),
                                                             port=os.environ.get('RABBIT_MQ_PORT'))
    # Logger
    app.config['GL_SERVER'] = os.environ.get("GL_SERVER", 'localhost')
    app.config['GL_PORT'] = int(os.environ.get("GL_PORT", 12201))
    app.config['ENABLE_GRAYLOG'] = int(os.environ.get('ENABLE_GRAYLOG', 0))
