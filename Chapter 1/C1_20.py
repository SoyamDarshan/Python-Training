# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:00:45 2018

@author: soyam

Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible order occurs with equal probability.
The random module includes a more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.



NOTE: Dont think this should be the final solution
"""

import random


def suffler(data):
    b=set()
    i=0
    while(i<data):
        
        b.add((random.randint(i,data)))
        i+=1
    return b    

print (suffler(6))    