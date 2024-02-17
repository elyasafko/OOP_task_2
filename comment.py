class Comment:
    def __init__(self, post, creator, content):
        self.post = post
        self.content = content
        self.creator = creator

    def get_content(self):
        return self.content

