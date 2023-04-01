# ds_protocol.py

# Carrie Liu
# carrihl1@uci.edu
# 64814057

import json


class DSPMessage:
    def __init__(self, request_type, username, password, message=None):
        self.request_type = request_type
        self.username = username
        self.password = password
        self.message = message

    def to_json(self):
        return json.dumps({"type": self.request_type,
                           "username": self.username,
                           "password": self.password,
                           "message": self.message})

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data["type"], data["username"],
                   data["password"], data["message"])

# import re
# from datetime import datetime

# class DSPMessage:
#     """Class representing a message exchanged with the DSP server."""

#     def __init__(self, message_string):
#         """Parse the message string and set the message attributes."""
#         # extract the message metadata and content
#         metadata, content = message_string.split('\n', 1)
#         # extract the message type, username, password, and timestamp
#         self.type, self.username, self.password,
#         timestamp = metadata.split(' ')
#         self.timestamp = datetime.fromisoformat(timestamp)
#         # set the message content
#         self.content = content.strip()

#     def __str__(self):
#         """Return a string representation of the message."""
#         timestamp_str = self.timestamp.isoformat(timespec='seconds')
#         return f"{self.type} {self.username}
#                  {self.password} {timestamp_str}\n{self.content}"

#     @classmethod
#     def create(cls, message_type, username, password, content):
#         """Create a new DSP message with the specified type,
#            username, password, and content."""
#         # create a timestamp for the message
#         timestamp = datetime.now()
#         # create the message metadata and content
#         metadata = f"{message_type} {username}
#         {password} {timestamp.isoformat()}"
#         message_string = f"{metadata}\n{content}"
#         # create and return the message object
#         return cls(message_string)
