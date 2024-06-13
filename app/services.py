from app.models import User, Message, ChatRoom
from app.schemas import UserSchema, MessageSchema, ChatRoomSchema

class UserService:
    def get_users(self):
        # Simulate database query
        users = [User(id=1, username='user1'), User(id=2, username='user2')]
        return UserSchema(many=True).dump(users)

    def get_user(self, user_id):
        # Simulate database query
        user = User(id=user_id, username=f'user{user_id}')
        return UserSchema().dump(user)

class MessageService:
    def get_messages(self, chat_room_id):
        # Simulate database query
        messages = [Message(id=1, user_id=1, text='Hello!', timestamp='2022-01-01 00:00:00'),
                    Message(id=2, user_id=2, text='Hi!', timestamp='2022-01-01 00:00:01')]
        return MessageSchema(many=True).dump(messages)

    def send_message(self, chat_room_id, user_id, text):
        # Simulate database query
        message = Message(id=3, user_id=user_id, text=text, timestamp='2022-01-01 00:00:02')
        return MessageSchema().dump(message)

class ChatRoomService:
    def get_chat_rooms(self):
        # Simulate database query
        chat_rooms = [ChatRoom(id=1, name='General', users=[User(id=1, username='user1'), User(id=2, username='user2')], messages=[])]
        return ChatRoomSchema(many=True).dump(chat_rooms)

    def get_chat_room(self, chat_room_id):
        # Simulate database query
        chat_room = ChatRoom(id=chat_room_id, name=f'Chat Room {chat_room_id}', users=[], messages=[])
        return ChatRoomSchema().dump(chat_room)