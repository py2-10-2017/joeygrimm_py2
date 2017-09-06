age = 35
def Hair(age):
    if age <= 18:
        print "You have a full head of hair"
    elif age <=25:
        print "You still have hair but its falling out fast."
    elif age <= 31:
        print "You have some hair but not much"
    else:
        print "You have no hair at all"


count = 1
while count < 13:
    print "counting and adding", count
    count +=1