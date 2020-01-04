'''
Max Of Three 
Exercise 28
Implement a function that takes as input three variables, and returns the largest of the three. 
Do this without using the Python max() function
'''

import random

def max_of_three(a, b, c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

def test_max_of_three():
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    if max([a, b, c]) != (max_of_three(a,b,c)):
        print(a, b, c)

for _ in range(0,100):
    test_max_of_three()