import unittest
from app.routes import app
import json

class TestRoutes(unittest.TestCase):
    def test_get_users(self):
        tester = app.test_client(self)
        response = tester.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)

    def test_get_user(self):
        tester = app.test_client(self)
        response = tester.get('/users/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['username'], 'user1')

    def test_get_chat_rooms(self):
        tester = app.test_client(self)
        response = tester.get('/chat_rooms')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)

    def test_get_chat_room(self):
        tester = app.test_client(self)
        response = tester.get('/chat_rooms/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'Chat Room 1')

    def test_get_messages(self):
        tester = app.test_client(self)
        response = tester.get('/chat_rooms/1/messages')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)

    def test_send_message(self):
        tester = app.test_client(self)
        data = {'user_id': 1, 'text': 'Hello!'}
        response = tester.post('/chat_rooms/1/messages', json=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['id'], 3)
        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['text'], 'Hello!')