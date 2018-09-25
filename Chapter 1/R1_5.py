# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:39:56 2018

@author: soyam

Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.
"""
del sum
def squareSum(n):
    try:
        result=sum(k*k for k in range(1,n+1,1) if (k*k<n))
        return result
    except Exception as e:
        print (e)

print(squareSum(10))