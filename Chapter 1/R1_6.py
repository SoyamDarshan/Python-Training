# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:22:57 2018

@author: soyam

Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

"""

def squareSum(n):
    arr=[]
    sum=0    
    for i in range(1,n):
        if (i % 2 != 0):
            arr.append(i*i) 
    for i in arr:
        sum+=i
    return sum    

n=10
result=(squareSum(n))

print (result)    
