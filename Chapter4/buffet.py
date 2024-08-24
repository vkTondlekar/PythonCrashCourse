# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 20:56:54 2023

@author: vtondlekar

A buffet-style restaurant offers only five basic foods. Think of five simple 
foods, and store them in a tuple
"""

buffet = ('corn fry','paneer65','dosa','idli','manchurian')

#Use a for loop to print each food the restaurant offers. 

print("Restaurant offers these five dishes:  ")
for item in buffet:
    print(" ",item)

#The restaurant changes its menu, replacing two of the items with different 
#foods. Add a line that rewrites the tuple, and then use a for loop to print 
#each of the items on the revised menu.

buffet = ('corn fry','paneer65','dosa','misal','samosa')

print("Restaurant offers these five dishes:  ")
for item in buffet:
    print(" ",item)
    
#Try to modify one of the items, and make sure that Python rejects the change

buffet[1] = 'misal'
