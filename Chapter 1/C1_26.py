# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 02:14:49 2018

@author: soyam

Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+ b = c,” “a = b− c,” or “a∗b = c.”
"""

def arithmetic(a,b,c):
    if(a+b==c):
        print("'a+ b = c' holds true")
    elif(a==b-c):
        print("'a = b− c' holds true")    
    elif(a*b==c):
        print("'a∗b = c' holds true")
    else:
        print("Properties dont hold true")    
        
arithmetic(10,15,5)        