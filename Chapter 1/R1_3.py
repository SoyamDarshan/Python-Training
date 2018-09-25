# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:42:18 2018

@author: Soyam

Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
"""

def minmax(arr):
    mini=arr[0]
    maxi=arr[0]
    for i in arr:
        mini = i if (mini>i) else mini
        maxi = i if (maxi<i) else maxi
    return (mini,maxi)

print(minmax([3]))    