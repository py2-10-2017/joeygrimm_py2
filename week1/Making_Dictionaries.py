My_info = {"Name": "Joey", "Age": 31, "State": "Kansas", "Pet": "Yogi"}

def Dict_Info(dict):
    print "Hello my name is", dict["Name"], "and I am", dict["Age"], "years old!"
    print "I am from the state of", dict["State"], "and reside in the state of", dict["State"], "."
    print "I have a dog named", dict["Pet"], "."

Dict_Info(My_info)