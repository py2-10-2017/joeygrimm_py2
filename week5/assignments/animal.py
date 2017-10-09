class Animal(object):
    def __init__(self, name, health=50):
        self.name = name
        self.health = health
    def Run(self):
        self.health -= 5
        print "You're running.\n"
        return self
    def Walk(self):
        self.health -= 1
        print "You're walking.\n"
        return self
    def Display_Health(self):
        print "{} has {} health.\n".format(self.name, self.health)
        return self

raccoon = Animal("Raccoon", 30)
raccoon.Display_Health().Walk().Walk().Walk().Run().Run().Display_Health()


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, health=150)
    def Pet(self):
        self.health += 5
        print "You received a pet for being a good dog.\n"
        return self

rocco = Dog("Rocco")
rocco.Display_Health().Walk().Walk().Walk().Run().Run().Pet().Display_Health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, health=170)
        self.health = 170
    def Eat(self):
        self.health += 5
        print "You just ate large goat..\n"
        return self
    def Fly(self):
        self.health -= 10
        print "You flew away.\n"
        return self
    def Display_Health(self):
        print "You're a dragon named {}.You have {} health.\n".format(self.name, self.health)
        return self

drogon = Dragon("Drogon")

drogon.Display_Health().Walk().Walk().Walk().Run().Run().Fly().Display_Health().Eat().Display_Health()