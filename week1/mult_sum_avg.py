
for i in range(1, 1000, 2):
    print(i) #this block of code starts with 1, is told to stop at 1000, and adds two to i with each iteration

'''
a = 0
b = 0
def multiples(a,b):
    a = 5
    b = 5
    while a < 1000000:
        a = a * b
        print a

multiples(a,b) #This function uses a while loop to times a by b until reaching 1000000. Not sure if this is what is needed in this portion of the assignment


def mult5():
    for c in range(5,1000000, 5):
        print c
mult5() #This simple function just adds 5 to c, which is initially has a value of 5 and prints it to the console. 
'''
r = [1,2,4,10,255,3]
print sum(r) #The sum() feature adds the values in the list together.

q = [1,2,4,10,255,3]
print sum(q)/len(q) # The sum() feature is used, then is divide by the items in the list(6) to get the average.