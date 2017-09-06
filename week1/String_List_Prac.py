words = "It's Thanksgiving day. It's my birthday, too!"
print words
print words.find('birthday')
words = words.replace('birthday', 'wedding anniversary')
print words

x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero....I'm still confused on how this works
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length.....same here
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list