# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 23:45:12 2018

@author: soyam

Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.

Note : What I think the question asks is that we write a reverse function and then compare
it with the arr[::-1] of Python.
 
"""

def reverse(arr):
    
    b=(arr[x] for x in range(len(arr)-1,-1,-1))
    return list(b)

arr="Soyam"
print (reverse(arr))


#PYTHON VERSION

c=arr[::-1]
print(c)