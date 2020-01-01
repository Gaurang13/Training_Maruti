'''def get_data(uerId):

    import karix
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
        data_validation(api_response)
    except ApiException as e:
        return "Exception when calling WebhookApi->get_webhook_by_id: %s\n" % e'''


def data_validation(api_response):

    import json
    from marshmallow import ValidationError
    from ..common.queue_helper import publish_message
    from ..common.constant import QueueEnum
    from ..manage import app_init_task


    #with open("path") as json_file:
        #json_schema = json.load(json_file)
    from marshmallow import Schema, fields

    UserSchema = Schema.from_dict(
        {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
    )

    try:
        app_init_task()
        payload = UserSchema.load({"name": "John", "email": "foo@gmail.com"})
        publish_message(QueueEnum.SEND_MESSAGE.value['route'], payload=payload)
    except ValidationError as err:
        print(err.messages)
        print(err.valid_data)