# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 00:13:18 2018

@author: soyam

Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).

NOTE: Couldnt figure out why it didnt work as it should have
"""

arr=[]
FLAG=True
while(FLAG):
    try:
        a=input()
        arr.insert(0,a)
        print(len(arr))
    except EOFError:
        raise("Value error")
        break
print("out of loop")        
for i in arr:
    print(i)
