from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.following = set()
        self.followers = set()
        self.is_online = True
        self.posts = []
        self.notifications = []

    def follow(self, user):
        if user.is_online:
            self.following.add(user)
            user.followers.add(self)
            print(self.username + " started following " + user.username)
        else:
            print(user.username + " is not online")

    def unfollow(self, user):
        if user.is_online:
            self.following.remove(user)
            user.followers.remove(self)
            print(self.username + " unfollowed " + user.username)
        else:
            print(user.username + " is not online")

    def print_notifications(self):
        print(self.username + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def log_out(self):
        if self.is_online:
            self.is_online = False
        else:
            print(self.username + " is already offline")

    def publish_post(self, post_type, content, price=None, location=None):
        if self.is_online:
            post = create_post(self, post_type, content, price, location)
            self.posts.append(post)
            print(post)
            """
            Observers pattern: notify all followers about the new post
            """
            for user in self.followers:
                user.notifications.append(self.username + " has a new post")
            return post

    def __str__(self):
        return "User name: " + self.username + ", Number of posts: " + str(
            len(self.posts)) + ", Number of followers: " + str(len(self.followers))


def create_post(owner, post_type, content=None, price=None, location=None):
    if post_type == "Text":
        return TextPost(owner, content)
    elif post_type == "Image":
        return ImagePost(owner, content)
    elif post_type == "Sale":
        return SalePost(owner, content, price, location)
    else:
        return None

