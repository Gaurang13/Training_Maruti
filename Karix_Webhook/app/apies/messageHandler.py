from abc import ABC
from marshmallow import ValidationError
from app.common.predefineSchema import whatsapp_schema
from flask_restful import marshal
from app.common.predefineSchema import message_format_schea
import logging
logger = logging.getLogger(__name__)


class messageTaskHandler(ABC):

    # Validate whatsapp data with predefine schema
    def schema_validation(self, whatsapp_data):
        pass

    # Fatching whatsapp message from karix with given token and udi
    def whatsapp_incoming_message_handler(self, fetched_uid, auth_id, auth_token):
        pass

    # Convert incoming message in specific format
    def message_converter(self, whatsapp_data):
        pass


class messageHepler(messageTaskHandler):

    def schema_validation(self, whatsapp_data):

        try:
            result = whatsapp_schema().load(whatsapp_data)
            return True
        except ValidationError as err:
            logging.error(err.messages)

    def whatsapp_incoming_message_handler(self, fetched_uid, auth_id, auth_token):
        import karix
        from karix.rest import ApiException

        # Configure HTTP basic authorization: basicAuth
        configuration = karix.Configuration()
        configuration.username = 'auth_id'
        configuration.password = 'auth_token'

        # create an instance of the API class
        api_instance = karix.MessageApi(karix.ApiClient(configuration))
        uid = 'fetched_uid'  # str | Alphanumeric ID of the message to get.
        api_version = '2.0'

        try:
            # Get message details by id.
            api_response = api_instance.get_message_by_id(uid, api_version=api_version)

            '''if api_response['data']['error']['code'] == 200 and api_response['data']['channel']' == "whatsapp":
                return api_response'''

        except ApiException as e:
            logger.error("Exception when calling MessageApi->get_message_by_id: %s\n" % e)

    def message_converter(self, whatsapp_incoming_message):

        return marshal(whatsapp_incoming_message, message_format_schea()), 200
