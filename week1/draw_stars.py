#Create a function called draw_stars() that takes a list of numbers and prints out *.

def draw_stars(lst):
    output = "*"
    char = ""
    for i in range(len(lst)):
        if isinstance(lst[i], str):
            char = lst[i][0].lower()
            print char * len(lst[i]) 
        else:
            print output * lst[i] 
    
a = [12,4,9,"Prime Rib"]
draw_stars(a)