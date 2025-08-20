class Post:
    def __init__(self, id, title=None, subtitle=None, body=None):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body

    def __repr__(self):
        return f"<Post {self.id}: {self.title}>"
