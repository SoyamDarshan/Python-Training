# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:30:48 2018

@author: soyam

Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

"""

def squareSum(n):
    arr=[]
    sum=0    
    for i in range(n+1):
        if (i*i < n):
            arr.append(i*i) 
    for i in arr:
        sum+=i
    return sum    

n=10
result=(squareSum(n))

print (result)    