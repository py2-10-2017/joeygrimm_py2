'''Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
Use the python built-in round function to convert that floating point number into an integer'''
import random

def coin_tosses():
    heads_count = 0
    tails_count = 0
    heads = 1
    tails = 2
    for i in range(0, 5000):
        print "Attempt ", i, ":",
        x = random.randint(1,2)
        if x is heads:
            heads_count += 1
            print "This coin toss is heads. You have tossed " + str(heads_count) + " heads and " + str(tails_count)+ " tails."
        else:
            tails_count += 1
            print "This coin toss is tails. You have tossed " + str(heads_count) + " heads and " + str(tails_count) + " tails."

coin_tosses()