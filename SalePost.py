from Post import Post


class SalePost(Post):

    def __init__(self, owner, content, price, location):
        super().__init__(owner, content)
        self.__price = price
        self.__location = location
        self.__is_sold = False

    def display(self):
        pass
        # need a work

    def sold(self, password):
        if self._owner.equal_password(password):
            self.__is_sold = True
            print(self._owner.username + "'s" + " product is sold")
        else:
            print("Incorrect password")

    def discount(self, percent, password):
        if self._owner.equal_password(password):
            self.__price = self.__price - self.__price * percent / 100
            print("Discount on " + self._owner.username + " product! the new price is: " + str(self.__price))

    def __str__(self):
        if self.__is_sold:
            return self._owner.username + " posted a product for sale:\n" + "Sold! " + self._content + ", price: " + str(
                self.__price) + ", pickup from: " + self.__location + "\n"
        else:
            return self._owner.username + " posted a product for sale:\n" + "For sale! " + self._content + ", price: " + str(
                self.__price) + ", pickup from: " + self.__location + "\n"
