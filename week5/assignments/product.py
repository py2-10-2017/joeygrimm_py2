class Product(object):
    def __init__(self, price, name, weight, brand, cost, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = self.price * self.weight
        self.status = status
        self.status = "For Sale"
    def Sell(self):
        self.status = "Sold"
        return self
    def AddTax(self):
        tax = self.cost *.09
        self.cost = self.cost + tax
        if self.cost < 0:
            self.cost = 0
        return self
    def Return(self):
        print "If the return is defective, type 'defective'. If the product is in the box, type 'in the box'\n"
        message = raw_input('product is: \n')
        if message == "defective":
            self.status = "defective"
            self.cost = 0
            print "Return allowed.\n"
            return self
        elif message == "in the box":
            self.status ="For Sale"
            discount= self.cost * .20
            self.cost = self.cost - discount
            print "Return allowed.\n"
            return self
        else:
            print "Return not allowed.\n"
            return self
    def display_all(self):
        print "Item Brand: {}".format(self.brand)
        print "Item Name: {}".format(self.name)
        print "Item Price per Pound: {}".format(self.price)
        print "Item Weight in Pounds: {}".format(self.weight)
        print "Item Cost: {}".format(self.cost)
        print "Item Status: {}\n".format(self.status)
        return self

banana = Product(1, "Banana",2, "Aldi", 2, "For Sale")
banana.AddTax().Sell().display_all()

apple = Product(2.85, "Apple", 3, "HyVee", 7,"For Sale")
apple.display_all().AddTax().Sell().Return().display_all()

carrot= Product(.55, "Carrot", 4, "Price Chopper", 2, "For Sale")
carrot.display_all().AddTax().Sell().Return().AddTax().Sell().display_all()
