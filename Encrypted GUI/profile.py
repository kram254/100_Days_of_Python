import json


class Profile:
    def __init__(self, username: str, password: str, bio: str = ""):
        self.username = username
        self.password = password
        self.bio = bio
        self.posts = []

    def add_post(self, title: str, content: str):
        self.posts.append({'title': title, 'content': content})

    def edit_post(self, index: int, title: str, content: str):
        self.posts[index] = {'title': title, 'content': content}

    def to_dict(self):
        return {'username': self.username, 'password': self.password, 'bio': self.bio, 'posts': self.posts}

    @classmethod
    def from_dict(cls, data: dict):
        username = data['username']
        password = data['password']
        bio = data['bio'] if 'bio' in data else ""
        profile = cls(username, password, bio)
        for post in data['posts']:
            profile.add_post(post['title'], post['content'])
        return profile

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, data: str):
        return cls.from_dict(json.loads(data))

    def __repr__(self):
        return f"<Profile {self.username}>"
