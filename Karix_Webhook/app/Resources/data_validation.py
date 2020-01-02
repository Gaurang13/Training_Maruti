from abc import ABC
import logging
log = logging.getLogger(__name__)

class webhookObject(ABC):

    def get_data(self,useId):
        pass
    def data_validation(self,api_response):
        pass

class webhookDataObject(webhookObject):

    def get_data(self,uerId):

        '''import karix
        from karix.rest import ApiException

        # Configure HTTP basic authorization: basicAuth
        configuration = karix.Configuration()
        configuration.username = 'YOUR_USERNAME'
        configuration.password = 'YOUR_PASSWORD'

        # create an instance of the API class
        api_instance = karix.WebhookApi(karix.ApiClient(configuration))
        uid = uerId  # str | Alphanumeric ID of the webhook to get.
        api_version = '2.0'  # str | API Version. If not specified your pinned verison is used. (optional) (default to 2.0)

        try:
            # Get a webhook by ID
            api_response = api_instance.get_webhook_by_id(uid, api_version=api_version)
        except ApiException as e:'''
        return ({"name": "John", "email": "foo@gmail.com" }) #"Exception when calling WebhookApi->get_webhook_by_id: %s\n" % e


    def data_validation(self,api_response):

        import json
        from marshmallow import ValidationError
        from ..common.queue_helper import publish_message
        from ..common.constant import QueueEnum


        #with open("path") as json_file:
            #json_schema = json.load(json_file)
        from marshmallow import Schema, fields

        '''UserSchema = Schema.from_dict(
            {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
        )'''

        try:

            #payload = {"name": "John", "email": "foo@gmail.com" }
            publish_message(QueueEnum.SEND_MESSAGE.value['route'], payload=api_response)#payload) #Passing the data to rebbit Mq
        except ValidationError as err:
            log.error(err.messages)
            log.error(err.valid_data)