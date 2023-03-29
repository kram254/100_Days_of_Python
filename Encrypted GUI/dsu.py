import requests
from requests.exceptions import HTTPError


class DSUClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def list_posts(self):
        try:
            response = requests.get(f"{self.base_url}/posts")
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return []
        except Exception as err:
            print(f"Other error occurred: {err}")
            return []

    def create_post(self, title, body, author):
        try:
            response = requests.post(
                f"{self.base_url}/posts",
                json={"title": title, "body": body, "author": author},
            )
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Other error occurred: {err}")
            return None

    def get_post(self, post_id):
        try:
            response = requests.get(f"{self.base_url}/posts/{post_id}")
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Other error occurred: {err}")
            return None

    def update_post(self, post_id, title, body):
        try:
            response = requests.put(
                f"{self.base_url}/posts/{post_id}",
                json={"title": title, "body": body},
            )
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"Other error occurred: {err}")
            return None

    def delete_post(self, post_id):
        try:
            response = requests.delete(f"{self.base_url}/posts/{post_id}")
            response.raise_for_status()
            return True
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return False
        except Exception as err:
            print(f"Other error occurred: {err}")
            return False
