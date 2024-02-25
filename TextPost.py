from Post import Post


class TextPost(Post):
    def __init__(self, owner, content):
        super().__init__(owner, content)

    def __str__(self):
        return self._owner.username + " published a post:\n" + '"' + self._content + '"' + "\n"
