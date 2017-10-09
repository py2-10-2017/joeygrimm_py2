'''
Create a class called  Car. 
In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage.
 If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. 
In the class have a method called display_all() that returns all the information about the car as a string. 
In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.
'''

class Car(object):
    def __init__(self, name, price, speed, fuel, milage):
        self.name = name
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage 
    def display_all(self):
        if self.price > 10000:
            taxes = "15%"
            total = self.price * .15
            after_tax_price = total + self.price
        else:
            taxes = "12%"
            total = self.price * .12
            after_tax_price = total + self.price
        print "Name: {}".format(self.name)
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Milage: {}".format(self.milage)
        print "Taxes: {}".format(taxes)
        print "After Tax Price: {}\n".format(after_tax_price)
        return self
        
                        



car1 = Car("Buick", 15000, 100, "Not Full", 35000)
car1.display_all()

car2 = Car("Mercedes",75000,160,"Full Tank",0)
car2.display_all()

car3= Car("Ford", 18000, 120, "Half Full", 45000)
car3.display_all()

car4 = Car("Subaru", 5000, 100, "Empty", 175000)
car4.display_all()

car5 = Car("Chevrolet", 25000, 140, "Full Tank", 65000)
car5.display_all()

car6 = Car("Dodge", 7500,95,"Quarter of a Tank", 115000)
car6.display_all()
