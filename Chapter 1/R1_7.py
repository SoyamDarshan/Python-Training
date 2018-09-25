# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:24:49 2018

@author: soyam

Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
"""
def squareSum(n):
    result=sum(k*k for k in range(n+1) if ( k % 2 !=0 ))
    return result


print(squareSum(10))
