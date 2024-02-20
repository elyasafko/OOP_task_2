from comment import Comment


class Post:

    def __init__(self, owner, content):
        self.owner = owner
        self.content = content
        self.likes = set()
        self.comments = []

    def like(self, user):
        if user.is_online:
            self.likes.add(user)
            if user != self.owner:
                self.owner.notifications.append(user.username + " liked your post")
                print("notification to " + self.owner.username + ": " + user.username + " liked your post")

    def comment(self, user, text):
        if user.is_online:
            comm = Comment(self, user, text)
            self.comments.append(comm)
            if user != self.owner:
                self.owner.notifications.append(user.username + " commented on your post")
                print("notification to " + self.owner.username + ": " + user.username + " commented on your post: " + text)

