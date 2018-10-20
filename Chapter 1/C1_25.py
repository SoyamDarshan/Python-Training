# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 02:08:07 2018

@author: soyam

Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example, 
if given the string "Let's try, Mike.", this function would return
"Lets try Mike".

"""

import re

s="Let's try, Mike."

regexPattern=r'[a-zA-Z\s0-9]*'

text=re.findall(regexPattern,s)
print('{}.'.format(''.join(text)))