# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:27:11 2018

@author: soyam

Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization
similar to the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""

import random


print (random.randrange(0,100,2))