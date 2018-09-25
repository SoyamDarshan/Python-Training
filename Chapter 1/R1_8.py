# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:44:18 2018

@author: soyam

Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index
 j ≥ 0 such that s[j] references the same element?
"""

s=input().strip()
k=int(input("K should be -{} <= k < 0 : ".format(len(s)-1)))
j=len(s)-k-1
print (j)
s1=s[::-1]
print("The string : {}\nThe value of s[k] for index −n ≤ k < 0 : {}\nThe equivalent j>=0 such that s[j] references the same element : {}".format(s,s1[k],s[j]))