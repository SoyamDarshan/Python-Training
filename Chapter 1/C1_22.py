# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 01:25:29 2018

@author: soyam

Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n− 1.

"""

def dotproduct(a,b):
    c=[a[i]*b[i] for i in range(len(a))]
    return c


print(dotproduct([1,2,3],[4,5,6]))