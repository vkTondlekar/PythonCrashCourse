# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:33:53 2023

@author: vtondlekar

A number raised to the third power is called a cube. For 
example,the cube of 2 is written as 2**3 in Python. Make 
a list of the first 10 cubes (that is, the cube of each 
integer from 1 through 10), and use a for loop to print 
out the value of each cube.
"""

cubes=[]
for i in range(1,11):
    #i=i**3
    cubes.append(i**3)
print(cubes)