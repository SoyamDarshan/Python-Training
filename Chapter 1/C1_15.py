# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 01:03:44 2018

@author: soyam

Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

def distinctNumbers(arr):
    arrDistinct=[]
    """
    for i in arr:
        if(i not in arrDistinct):
            arrDistinct.append(i)
    """
    [arrDistinct.append(x) for x in arr if(x not in arrDistinct)]

    return arrDistinct


arr=[1,23,3,45,6,67,8,8,9,1,3]

print(distinctNumbers(arr))     



##PYTHON WAY
print(set(arr))       