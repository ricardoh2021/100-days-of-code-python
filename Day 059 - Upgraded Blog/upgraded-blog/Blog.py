class Blog:
    def __init__(self, id, title=None, subtitle=None, body=None, image_url=None, date=None, author=None):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.image_url = image_url
        self.date = date
        self.author = author

    def __repr__(self):
        return f"<Post {self.id}: {self.title}>"
