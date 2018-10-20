# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 01:31:51 2018

@author: soyam

Give an example of a Python code fragment that attempts to write an element to a list 
based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”

NOTE :This Wont work if arr.insert(a,b) is used
"""

arr=[1,2,3,4,5]
while 1:
    try:
        a,b=map(int,input("index,element ").split())
        arr[a]=b
        print(arr)
    except IndexError:    
        print("Don’t try buffer overflow attacks in Python!")
        break
print (arr)    