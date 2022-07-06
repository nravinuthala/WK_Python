class Computer:

    def __init__(self, price):
        # self.maxprice = price
        self.__maxprice = price

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def get_max_price(self):
        return self.__maxprice

    def set_max_price(self, price):
        self.__maxprice = price
    #
    @property
    def maxprice(self):
        return self.__maxprice

    # maxprice = property(get_max_price)
    #
    @maxprice.setter
    def maxprice(self, val):
        self.__maxprice = val

c = Computer(50000)
# c.sell()
#
# # # change the price
# # c.__maxprice = 55000
# # print(c.__dict__)
# # c.sell()
# #
# print(c.get_max_price())
# # # using setter function
# c.setMaxPrice(55000)
# c.sell()
# #
# # print(c.maxprice)
# # c.maxprice = 100000
# # print(c.maxprice)

#print(c.get_max_price())
# c.set_max_price(20000)
# print(c.get_max_price())

print(c.maxprice)
c.maxprice = 20000
print(c.maxprice)