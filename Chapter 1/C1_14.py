# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:49:14 2018

@author: soyam

Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def checkODD(arr):
    result=((arr[a],arr[b]) for a in range(0,len(arr)-1) for b in range(1,len(arr)) if (arr[a]*arr[b]%2!=0 and a!=b and b>a) )
    
    return list(result)

arr=[1,2,3,4,5,6]

print(checkODD(arr))