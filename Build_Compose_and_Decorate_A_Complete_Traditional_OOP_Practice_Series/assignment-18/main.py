# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting Price..")
        return self._price
    
    @price.setter
    def price(self, value):
        print("Setting Price..")
        self._price = value
    
    @price.deleter
    def price(self):
        print("deleting")
        del self._price


p1 = Product(100)
p1.price = 200
print(p1.price)
del p1.price