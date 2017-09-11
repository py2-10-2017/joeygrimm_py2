def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def names(lst):
    print namestr(lst, globals())
    for i in lst:
        print i['first_name'], i['last_name']

Students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

Instructors =  [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]

#names(Students)
#names(Instructors)

# This my original code prior to start the users portion
def User_Names(dic):
     for some_key, some_value in dic.iteritems():
        counter = 0
        if some_key is "Students":
            print "\n"
            print some_key
            for i in some_value:
                counter += 1
                print "\t", counter, i['first_name'], i['last_name'], len(i['first_name']) + len(i['last_name'])
        else:
            print "\n"
            print some_key
            for i in some_value:
                counter += 1
                print "\t", counter, i['first_name'], i['last_name'], len(i['first_name']) + len(i['last_name'])
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print User_Names(users)
