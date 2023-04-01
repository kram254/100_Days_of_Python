import socket
import json

HOST = '127.0.0.1'
PORT = 65432

def ds_protocol(message, recipient):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Creating the message packet
        packet = {
            'type': 'message',
            'message': message,
            'recipient': recipient
        }

        # Sending the packet to the DSP server
        s.sendall(json.dumps(packet).encode('utf-8'))

        # Receiving the response from the recipient
        data = s.recv(1024)

    return data.decode('utf-8')

class Profile:
    def __init__(self, username):
        self.username = username
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)

    def get_friends(self):
        return self.friends

class Message:
    def __init__(self, text, recipient):
        self.text = text
        self.recipient = recipient

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_recipient(self):
        return self.recipient

    def set_recipient(self, recipient):
        self.recipient = recipient


class DS_Messenger:
    def __init__(self, username):
        self.profile = Profile(username)

    def send_message(self, message):
        ds_protocol(message.get_text(), message.get_recipient())

    def receive_message(self, message):
        ds_protocol(message.get_text(), message.get_recipient())

    def add_friend(self, friend):
        self.profile.add_friend(friend)

    def remove_friend(self, friend):
        self.profile.remove_friend(friend)

    def get_friends(self):
        return self.profile.get_friends()


if __name__ == '__main__':
    # Example usage
    messenger = DS_Messenger('Mark')
    message = Message('Hello Karios!', 'Karios')
    messenger.send_message(message)
