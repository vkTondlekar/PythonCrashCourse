# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:27:51 2023

@author: vtondlekar

Make a list of the multiples of 3, from 3 to 30. 
Use a for loop to print the numbers in your list.
"""

list = []
for i in range(3,31):
    if (i%3)==0:
        list.append(i)
print(list)