from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    dimensions = fields.Dict(keys=fields.Str(), values=fields.Float(), required=True)
    image_url = fields.Url(required=False)

class LayoutSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    items = fields.List(fields.Nested(ItemSchema), required=True)
    layout = fields.Dict(keys=fields.Str(), values=fields.Dict(), required=True)
    created_at = fields.DateTime(dump_only=True)