from dataclasses import dataclass
from typing import List

@dataclass
class User:
    id: int
    username: str

@dataclass
class Message:
    id: int
    user_id: int
    text: str
    timestamp: str

@dataclass
class ChatRoom:
    id: int
    name: str
    users: List[User]
    messages: List[Message]