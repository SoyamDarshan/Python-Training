# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 02:04:20 2018

@author: soyam

Write a short Python function that counts the number of vowels in a given
character string.
"""

s=input()
counter=0
vowels=['a','e','i','o','u']
counter=[s.count(i) for i in vowels]

print( sum(counter))