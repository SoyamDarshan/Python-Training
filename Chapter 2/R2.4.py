# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 01:46:59 2018

@author: soyam


Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.

"""

class Flower:
    def __init__(self,name,numberOfpetals,var):
        self._name=name
        self._numberOfpetals=numberOfpetals
        self._var=var
        
        
    def __str__(self):
        return (self._name)
    
    def __int__(self):
        return (self._numberOfpetals)
    
    def __float__(self):
        return (self._var)
    
    
    
if __name__ == '__main__':
    v=Flower('rose',16,3.2)
    #value
    print(v)
    print(v._name)
    print(v._numberOfpetals)
    print(v._var)
    #object 
    print(v.__str__)
    print(v.__int__)
    print(v.__float__)
    #value
    print(v.__str__())
    print(v.__int__())
    print(v.__float__())
    #value v.__str__() == str(v)
    print(str(v))
    print(int(v))
    print(float(v))