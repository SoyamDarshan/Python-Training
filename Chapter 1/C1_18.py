# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 04:40:58 2018

@author: soyam

Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].


"""
arr=[]
[arr.append(x*(x-1))  for x in range(1,11)]
print (arr)