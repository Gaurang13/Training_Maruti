from pprint import pprint

from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email()
    created_at = fields.DateTime()



try:
    result = UserSchema().load({"email": "foo@bar.com"})
except ValidationError as err:
    pprint(err.messages)