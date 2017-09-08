Dave = ['smells badly', 34, "Chicago"]
Clarence = ['has not shaved in weeks','unknown','Barcelona']
Ralph = [19, 43, 6117]

def String_Number(lst):
    total = 0
    string = ""

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value 
        elif isinstance(value, str):
            string += value

    if string and total:
        print "This is a mixed type of list"
        print "String:", string
        print "Total:", total

    elif string:
        print "This is a string type of list"
        print "String:", string

    else:
        print "This is either of int/float or float/int mixed type of list"
        print "Total", total

print String_Number(Dave)
print String_Number(Clarence)
print String_Number(Ralph)
