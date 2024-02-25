from matplotlib import image as mpimg
from Post import Post
import matplotlib.pyplot as plt


class ImagePost(Post):

    def __init__(self, owner, picture_path):
        super().__init__(owner, picture_path)

    def display(self):
        img = mpimg.imread(self._content)
        plt.imshow(img)
        plt.show()
        print("Shows picture")

    def __str__(self):
        return self._owner.username + " posted a picture" + "\n"
