# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 04:44:49 2018

@author: soyam

Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.



Note : ASCII value for 'a' is 97
chr() function takes that integer(the Unicode code point of the character) value and provides us with the character
ord() function takes that character value and provides us with the integer(the Unicode code point of the character)
    
"""

arr=[]
[arr.append(chr(x)) for x in range(97,123)]
print (arr)

