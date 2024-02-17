from Post import Post


class SalePost(Post):

    def __init__(self, owner, content, price, location):
        super().__init__(owner, content)
        self.price = price
        self.location = location
        self.is_sold = False

    def display(self):
        pass
        # need a work

    def sold(self, password):
        if self.owner.password == password:
            self.is_sold = True
            print(self.owner.username + "'s" + " product is sold")
        else:
            print("Incorrect password")

    def discount(self, percent, password):
        if self.owner.password == password:
            self.price = self.price - self.price * percent / 100
            print("Discount on " + self.owner.username + " product! the new price is: " + str(self.price))

    def __str__(self):
        if self.is_sold:
            return self.owner.username + " posted a product for sale:\n" + "Sold! " + self.content + ", price: " + str(
                self.price) + ", pickup from: " + self.location + "\n"
        else:
            return self.owner.username + " posted a product for sale:\n" + "For sale! " + self.content + ", price: " + str(
                self.price) + ", pickup from: " + self.location + "\n"
