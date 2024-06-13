import unittest
from app.models import User, Message, ChatRoom

class TestModels(unittest.TestCase):
    def test_user(self):
        user = User(id=1, username='user1')
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'user1')

    def test_message(self):
        message = Message(id=1, user_id=1, text='Hello!', timestamp='2022-01-01 00:00:00')
        self.assertEqual(message.id, 1)
        self.assertEqual(message.user_id, 1)
        self.assertEqual(message.text, 'Hello!')
        self.assertEqual(message.timestamp, '2022-01-01 00:00:00')

    def test_chat_room(self):
        chat_room = ChatRoom(id=1, name='General', users=[User(id=1, username='user1'), User(id=2, username='user2')], messages=[])
        self.assertEqual(chat_room.id, 1)
        self.assertEqual(chat_room.name, 'General')
        self.assertEqual(len(chat_room.users), 2)
        self.assertEqual(len(chat_room.messages), 0)