"""Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number."""

def odd_even(num):
    for i in range(1, num):
        if i % 2 == 0:
            print i, "This is an even number"
        else:
            print i, "This is an odd number"

odd_even(14)

'''Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.'''

def multiply(lst, num):
    newlist = []
    for i in range(len(lst)):
        lst[i] *= num
        newlist.append(lst[i])
    print newlist

numbers_list= [12,65,30,85]
multiply(numbers_list, 5)

'''Write a function that takes the multiply function call as an argument.
Your new function should return the multiplied list as a two-dimensional list.
Each internal list should contain the 1's times the number in the original list. 
'''

def multiple_layers(arr):
    new_arr = []
    for item in arr:
        inner_arr = []
        count = 0
        while count < item:
            inner_arr.append(1)
            count += 1
        new_arr.append(inner_arr)
    return new_arr

test = multiple_layers(multiply([23,5,33], 4))
print test