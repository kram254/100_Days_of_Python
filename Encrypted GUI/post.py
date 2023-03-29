import json


class Post:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def to_json(self):
        return json.dumps({
            'title': self.title,
            'body': self.body
        })

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['title'], data['body'])
    
    def edit_title(self, new_title):
        self.title = new_title
        
    def edit_body(self, new_body):
        self.body = new_body
