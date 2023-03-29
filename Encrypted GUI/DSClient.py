import requests
import json
import base64
from NaClProfile import NaClProfile
from Profile import Post

class DSClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.nacl_profile = NaClProfile()
        self.keypair = None
        self.server_public_key = None
        self.token = None

    def generate_keypair(self):
        self.keypair = self.nacl_profile.generate_keypair()

    def join(self, username, password):
        if not self.keypair:
            self.generate_keypair()

        # Join request with public key as token
        join_request = {
            "join": {
                "username": username,
                "password": password,
                "token": self.nacl_profile.public_key
            }
        }

        response = requests.post(
            f"{self.server_url}/join", json.dumps(join_request)
        )
        response_data = json.loads(response.content)

        # Store server's public key
        self.server_public_key = response_data["response"]["token"]

        if response_data["response"]["type"] == "ok":
            print(response_data["response"]["message"])
            self.token = response_data["response"]["token"]
        else:
            print("Join failed. Reason:", response_data["response"]["message"])

    def post(self, text):
        if not self.token:
            print("You must join the server before posting.")
            return

        # Encrypt post text
        encrypted_text = self.nacl_profile.encrypt_entry(text, self.server_public_key)

        # Create post request with encrypted text
        post_request = {
            "post": {
                "token": self.nacl_profile.public_key,
                "message": encrypted_text
            }
        }

        response = requests.post(
            f"{self.server_url}/post", json.dumps(post_request)
        )
        response_data = json.loads(response.content)

        if response_data["response"]["type"] == "ok":
            print(response_data["response"]["message"])
        else:
            print("Post failed. Reason:", response_data["response"]["message"])

    def get_posts(self):
        response = requests.get(f"{self.server_url}/get")
        response_data = json.loads(response.content)

        if response_data["response"]["type"] == "ok":
            posts = []
            for post_data in response_data["response"]["posts"]:
                # Decrypt post text
                decrypted_text = self.nacl_profile.decrypt_entry(post_data["entry"])
                post = Post(
                    decrypted_text,
                    post_data["timestamp"],
                    post_data["username"]
                )
                posts.append(post)
            return posts
        else:
            print("Get posts failed. Reason:", response_data["response"]["message"])

    def exit(self):
        if not self.token:
            print("You must join the server before exiting.")
            return

        exit_request = {"exit": {"token": self.token}}

        response = requests.post(
            f"{self.server_url}/exit", json.dumps(exit_request)
        )
        response_data = json.loads(response.content)

        if response_data["response"]["type"] == "ok":
            print(response_data["response"]["message"])
        else:
            print("Exit failed. Reason:", response_data["response"]["message"])

if __name__ == "__main__":
    client = DSClient("http://localhost:5000")
    client.join("testuser", "testpassword")
    client.post("Hello world!")
    posts = client.get_posts()
    for post in posts:
        print(post)
    client.exit()
