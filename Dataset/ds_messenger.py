from ds_protocol import ds_protocol
from ds_exceptions import *

class DS_Messenger:   

    def __init__(self, username):
        self.username = username
        self.profile = Profile(username)

    def send_message(self, message_text, recipient):
        message = Message(message_text, recipient)
        try:
            response = ds_protocol(message.get_text(), message.get_recipient())
            return response
        except DSException as e:
            raise DSException(f"Error sending message: {e}")

    def receive_message(self, message_text, sender):
        message = Message(message_text, sender)
        try:
            response = ds_protocol(message.get_text(), message.get_recipient())
            return response
        except DSException as e:
            raise DSException(f"Error receiving message: {e}")

    def add_friend(self, friend):
        try:
            response = ds_protocol("add_friend", friend)
            self.profile.add_friend(friend)
            return response
        except DSException as e:
            raise DSException(f"Error adding friend: {e}")

    def remove_friend(self, friend):
        try:
            response = ds_protocol("remove_friend", friend)
            self.profile.remove_friend(friend)
            return response
        except DSException as e:
            raise DSException(f"Error removing friend: {e}")

    def get_friends(self):
        try:
            response = ds_protocol("get_friends", self.username)
            self.profile.friends = response.split(",")
            return self.profile.get_friends()
        except DSException as e:
            raise DSException(f"Error getting friend list: {e}")
