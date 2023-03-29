import socket
import json
from NaClProfile import NaClProfile

class DSProtocol:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port
        self.sock = None
        self.token = None
        self.np = None
        self.server_public_key = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def close(self):
        self.sock.close()

    def register(self, username, password):
        data = {"register": {"username": username, "password": password}}
        self.sock.sendall(json.dumps(data).encode())
        response = json.loads(self.sock.recv(1024).decode())
        if response["response"]["type"] == "error":
            return response["response"]["message"]
        else:
            self.token = response["response"]["token"]
            return True

    def join(self, username, password):
        self.connect()
        data = {"join": {"username": username, "password": password, "token": self.np.public_key}}
        self.sock.sendall(json.dumps(data).encode())
        response = json.loads(self.sock.recv(1024).decode())
        self.close()
        if response["response"]["type"] == "error":
            return response["response"]["message"]
        else:
            self.token = self.np.encrypt_entry(response["response"]["token"], self.server_public_key).decode()
            return True

    def post(self, message):
        data = {"post": {"message": self.np.encrypt_entry(message, self.server_public_key).decode(), "token": self.token}}
        self.sock.sendall(json.dumps(data).encode())
        response = json.loads(self.sock.recv(1024).decode())
        if response["response"]["type"] == "error":
            return response["response"]["message"]
        else:
            return True

    def get_posts(self):
        data = {"get_posts": {"token": self.token}}
        self.sock.sendall(json.dumps(data).encode())
        response = json.loads(self.sock.recv(1024).decode())
        if response["response"]["type"] == "error":
            return response["response"]["message"]
        else:
            posts = []
            for p in response["response"]["posts"]:
                posts.append(self.np.decrypt_entry(p["entry"]).decode())
            return posts

    def set_profile(self, profile):
        self.np = profile
        self.server_public_key = self.np.decrypt_key(response["response"]["token"]).decode()

    def get_profile(self):
        return self.np
