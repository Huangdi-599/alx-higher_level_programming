#!/usr/bin/python3
'''
   0-add_integer.py
   Contains a function that adds two integers
'''

def add_integer(a, b=98): 
    '''
    Python function to sum two integers, check if a/b is int & float
    '''
    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
