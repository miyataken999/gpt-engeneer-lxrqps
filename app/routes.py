from flask import Flask, request, jsonify
from app.services import UserService, MessageService, ChatRoomService

app = Flask(__name__)

user_service = UserService()
message_service = MessageService()
chat_room_service = ChatRoomService()

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_service.get_users())

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(user_service.get_user(user_id))

@app.route('/chat_rooms', methods=['GET'])
def get_chat_rooms():
    return jsonify(chat_room_service.get_chat_rooms())

@app.route('/chat_rooms/<int:chat_room_id>', methods=['GET'])
def get_chat_room(chat_room_id):
    return jsonify(chat_room_service.get_chat_room(chat_room_id))

@app.route('/chat_rooms/<int:chat_room_id>/messages', methods=['GET'])
def get_messages(chat_room_id):
    return jsonify(message_service.get_messages(chat_room_id))

@app.route('/chat_rooms/<int:chat_room_id>/messages', methods=['POST'])
def send_message(chat_room_id):
    data = request.get_json()
    user_id = data['user_id']
    text = data['text']
    return jsonify(message_service.send_message(chat_room_id, user_id, text))

if __name__ == '__main__':
    app.run(debug=True)