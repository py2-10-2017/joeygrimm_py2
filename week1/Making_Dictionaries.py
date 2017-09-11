My_info = {"Name": "Joey", "Age": 31, "State": "Kansas", "Pet": "Yogi"}

#This was my first the first function I made for this problem but after reviewing the solution code, I prefer using iteritems()

def Dict_Info(dict):
    print "Hello my name is", dict["Name"], "and I am", dict["Age"], "years old!"
    print "I am from the state of", dict["State"], "and reside in the state of", dict["State"], "."
    print "I have a dog named", dict["Pet"], "."

Dict_Info(My_info)


def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        if some_key is "Name":
            print "Hello my {} is {}.".format(some_key, some_value)
        elif some_key is "State":
            print "I am from the {} of {}.".format(some_key, some_value)
        elif some_key is "Age":
            print "My {} is {} years old.".format(some_key, some_value)
        else:
            print "My {} is named {}.".format(some_key, some_value)
   
print_dictionary_values(My_info)