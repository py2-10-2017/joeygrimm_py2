'''
Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
'''
import random
random_num = random.randint(55, 100)
def Score_grade(grade):
    for i in range(0, 10):
        grade = random.randint(55, 100)
        if grade > 90:
            print "Your grade is a A."
        elif grade > 80:
            print "Your grade is a B."
        elif grade > 70:
            print "Your grade is a C."
        elif grade > 60:
            print "Your grade is a D."
        else:
            print "Your grade is an F."

    print "The scoring game is done. Goodbye"

Score_grade(random_num)