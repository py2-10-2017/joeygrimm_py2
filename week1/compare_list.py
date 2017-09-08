'''
I want to make a function which can take in two parameters. 
It needs to total the parameters, 
then tell us which is large, smaller, or the same and print something.
'''

groceries = ["apples","bananas", "avocados", "turkey"]
groceries2 = ["apples","bananas", "avocados", "turkey"]
groceries3 = ["oranges","bananas", "avocados", "turkey"]

numberslist = [1,2,3,4,5]
numberslist2 = [1,2,3,4,5]
numberslist3 = [1,2,6,4,5]

def list_comparision(i, a):
    if i == a:
        print "These two lists are the same."
    elif i <= a:
        print "List {} is smaller than list {}".format(i,a)
    else:
        print "List {} is larger than list {}".format(i,a)

list_comparision(groceries3, groceries)
list_comparision(numberslist,numberslist2)
list_comparision(numberslist,groceries)