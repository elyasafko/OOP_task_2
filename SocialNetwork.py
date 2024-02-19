from User import User


class SocialNetwork:
    """
    # Here we use the Singleton pattern to ensure that only one instance of the SocialNetwork class is created
    """
    instance = None

    def __new__(cls, name):
        if cls.instance is None:
            cls.instance = super(SocialNetwork, cls).__new__(cls)
            print("The social network " + name + " was created!")
        return cls.instance

    def __init__(self, name):
        self.users = []
        self.name = name

    def sign_up(self, username, password):
        # Check if the username is already taken
        if self.get_user(username):
            print("username already taken")
            return None
        # Check if the password is valid
        if len(password) < 4 or len(password) > 8:
            print("password must be between 4 and 8 characters")
            return None
        # Create a new user
        user = User(username, password)
        self.users.append(user)
        return user

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def log_in(self, username, password):
        user = self.get_user(username)
        if user and user.password == password:
            user.is_online = True
            print(username + " connected")
        else:
            print("incorrect username or password")

    def log_out(self, username):
        user = self.get_user(username)
        if user is None:
            print("username not found")
            return
        user.log_out()
        print(username + " disconnected")

    def __str__(self):
        ans = self.name + " social network:\n"
        for user in self.users:
            ans += str(user) + "\n"
        return ans
