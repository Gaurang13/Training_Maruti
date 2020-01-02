from flask import Flask
from .config import configure_app
import logging
logger = logging.getLogger(__name__)

__all__ = ['create_app', 'app_init_rebbitmq', 'init_task']


def create_app():
    """Initialize Flask Application"""
    app = Flask(__name__)
    configure_app(app)
    # Config App Logger
    return app


def app_init_rebbitmq():
    from app import app
    with app.app_context():
        # Start RabbitMQ
        from app.common.queue_helper import queue_init
        queue_init()


def init_task(id):
    from app.database.model.fetchWhatsappData import fetch_whatsapp_data
    from app.apies.messageHandler import messageHepler
    from app.common.queue_helper import publish_message
    from app.common.constant import QueueEnum

    # Passing the id to fetch whatspp data from database
    whatsapp_data = fetch_whatsapp_data(id)

    helper = messageHepler()

    # return true if validate successful
    whatsapp_data_validation = helper.schema_validation(whatsapp_data)

    if whatsapp_data_validation:

        uid = "whatsapp_data['uid']"
        auth_token = "whatsapp_data['token']"
        auth_id = "whatsapp_data['auth_id']"
        # return message given by karix if status code is 200
        whatsapp_incoming_message = helper.whatsapp_incoming_message_handler(uid, auth_id, auth_token)

        if whatsapp_incoming_message:

            # retrun converted karix message into specific format
            converted_message = helper.message_converter(whatsapp_incoming_message)

            # Pushing message in rebbit mq for async process
            publish_message(QueueEnum.SEND_MESSAGE.value['route'], payload=converted_message)

        else:
            logger.error("Incoming message don't have status code 200 or don't have channel as whatsapp")

    else:

        logger.error("Incoming data is not in desired schema")
