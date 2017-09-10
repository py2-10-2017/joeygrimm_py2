'''
Write a program that prints a 'checkerboard' pattern to the console.
Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. In our case we will alternate stars and spaces. 
The goal is to repeat a process several times. This should make you think of looping.
Make a function that prints this out the checker board. Use a loop to make this happen.
'''

def checkerboard():
    a = " * * * *"
    b = "* * * * "
    for i in range (0, 4):
        print b
        print a

checkerboard()
