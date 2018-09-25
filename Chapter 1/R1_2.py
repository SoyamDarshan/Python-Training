# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:33:57 2018

@author: Soyam

Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):
    return False if (k&1) else True



print(is_even(5))