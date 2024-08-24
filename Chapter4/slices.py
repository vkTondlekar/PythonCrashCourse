# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:03:15 2023

@author: vtondlekar

Using one of the programs you wrote in this chapter, add several lines to 
the end of the program that do the following:Print the message The first 
three items in the list are:.Then use a slice to print the first three items
from that program’s list.
"""
domino_pizzas = ['corn', 'cheese', 'farm','chicken','paneer','onion','cucumber']

print(f"\n The first three pizzas are : {domino_pizzas[:3]}")


"""Print the message Three items from the middle of the list are:. Then use 
a slice to print three items from the middle of the list."""

print(f"\n The middle pizzas are: {domino_pizzas[2:5]}")

"""Print the message The last three items in the list are:. Then use a slice 
to print the last three items in the list."""

print(f"\n The last pizzas are: {domino_pizzas[-3:]}")