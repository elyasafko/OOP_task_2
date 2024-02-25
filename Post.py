from comment import Comment
from abc import ABC, abstractmethod


class Post(ABC):

    def __init__(self, owner, content):
        self._owner = owner
        self._content = content
        self._likes = set()
        self._comments = []

    def like(self, user):
        if user.is_online:
            self._likes.add(user)
            if user != self._owner:
                self._owner.notifications.append(user.username + " liked your post")
                print("notification to " + self._owner.username + ": " + user.username + " liked your post")

    def comment(self, user, text):
        if user.is_online:
            comm = Comment(self, user, text)
            self._comments.append(comm)
            if user != self._owner:
                self._owner.notifications.append(user.username + " commented on your post")
                print(
                    "notification to " + self._owner.username + ": " + user.username + " commented on your post: " + text)
