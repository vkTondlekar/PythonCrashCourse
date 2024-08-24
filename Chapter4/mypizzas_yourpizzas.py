# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:02:54 2023

@author: vtondlekar

Start with your program from Exercise 4-1 (page 56). Make a copy of the list 
of pizzas, and call it friend_pizzas. Then, do the following:

"""

my_pizzas = ['corn','onion','paneer']

"""    Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas """
friend_pizzas = my_pizzas[:]

friend_pizzas.append('cheese')
my_pizzas.append('farm')


"""Print the message My favorite pizzas are:, and then use a for loop to 
print the first list"""
print("My favourite pizzas are: ")
for pizza in my_pizzas:
    print(" ",pizza)
    
"""Print the message My friend’s favorite pizzas are:, and then use a for 
loop to print the second list """
print("\nMy friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(" ",pizza)