class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = True
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    def logout(self):
        self.logged = False
        print self.name + " is not logged in"
        return self
    def show(self):
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self

    '''
    __init__ is called when ever an object of the class is constructed.
     That means when ever we will create a student object we will see the message “A student object is created” in the prompt. 
     You can see the first argument to the method is self. 
     It is a special variable which points to the current object (like this in C++). 
     The object is passed implicitly to every method available in it, but we have to get it explicitly in every method while writing the methods.
      Example shown below. Remember to declare all the possible attributes in the __init__ method itself. 
      Even if you are not using them right away, you can always assign them as None.

      Attributes: Characteristics shared by all instances of the class type.
       Take our User class, for example. All users have a name and an email.
        You might be wondering how each user can have a different name and email. We'll show you in the following tab.
        Methods: Actions that an object can perform.
         A user, for example, might be able to make a purchase. A method is like a function that belongs to a class. 
         It's some instructions that will only work when called on an object that has been created from that class. We'll show you how shortly.
      '''