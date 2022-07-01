class Computer:

    def __init__(self, price):
        self.__maxprice = price

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer(50000)
c.sell()

# change the price
c.__maxprice = 55000
c.sell()

# using setter function
c.setMaxPrice(55000)
c.sell()