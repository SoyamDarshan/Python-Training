# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 01:36:09 2018

@author: soyam

In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?

"""
"""
we note that reassigning a new
value to a formal parameter with a function body, such as by setting data = [ ],
does not alter the actual parameter; such a reassignment simply breaks the alias.


"""