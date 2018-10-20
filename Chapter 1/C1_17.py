# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 02:29:50 2018

@author: soyam

Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
for val in data:
val = factor
Explain why or why not.

"""

def scale(data, factor):
    for val in data:
        val *= factor
        
    return data

print(scale([31,5,6,7,3,4,2],2))


"""
This won't work because there is no reassignment of value in the "data" list.

"""