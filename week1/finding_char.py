'''
I am not quite sure how the -1 works in this function. 
'''


def find_character(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):

        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])

    print new_list

test_list = ['hello','world','my','name','is','Joseph','Oreilly']
find_character(test_list, 'o')