from marshmallow import Schema, fields
from app.models import User, Message, ChatRoom

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()

class MessageSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    text = fields.Str()
    timestamp = fields.Str()

class ChatRoomSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    users = fields.Nested(UserSchema, many=True)
    messages = fields.Nested(MessageSchema, many=True)