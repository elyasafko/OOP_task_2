from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__following = set()
        self.__followers = set()  # this is the observer list
        self.is_online = True
        self.__posts = []
        self.notifications = []

    def follow(self, user):
        if user.is_online:
            self.__following.add(user)
            user.add_observer(self)
            print(self.username + " started following " + user.username)
        else:
            print(user.username + " is not online")

    def unfollow(self, user):
        if user.is_online:
            self.__following.remove(user)
            user.remove_observer(self)
            print(self.username + " unfollowed " + user.username)
        else:
            print(user.username + " is not online")

    def add_observer(self, observer):
        self.__followers.add(observer)

    def remove_observer(self, observer):
        self.__followers.remove(observer)

    """
    here we use the observer pattern to notify the followers when a new post is published
    """

    def notify_observers(self):
        for observer in self.__followers:
            observer.update(self.username + " has a new post")

    def update(self, notification):
        self.notifications.append(notification)

    def publish_post(self, post_type, content, price=None, location=None):
        if self.is_online:
            post = create_post(self, post_type, content, price, location)
            self.__posts.append(post)
            print(post)
            self.notify_observers()
            return post

    def print_notifications(self):
        print(self.username + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def log_out(self):
        if self.is_online:
            self.is_online = False
        else:
            print(self.username + " is already offline")

    def __str__(self):
        return "User name: " + self.username + ", Number of posts: " + str(
            len(self.__posts)) + ", Number of followers: " + str(len(self.__followers))

    def equal_password(self, password):
        if password == self.__password:
            return True
        else:
            return False


"""
here we use the factory pattern to create the different types of posts
"""


def create_post(owner, post_type, content=None, price=None, location=None):
    if post_type == "Text":
        return TextPost(owner, content)
    elif post_type == "Image":
        return ImagePost(owner, content)
    elif post_type == "Sale":
        return SalePost(owner, content, price, location)
    else:
        return None
