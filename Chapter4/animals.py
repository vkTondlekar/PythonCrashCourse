# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:48:20 2023

@author: vtondlekar

Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print 
out the name of each animal.

Modify your program to print a statement about each animal, such as A dog 
would make a great pet.Add a line at the end of your program, stating what 
these animals have in common. You could print a sentence, such as Any of 
these animals would make a great pet!
"""
animals = ['dog','cat','rabbit']

for animal in animals:
    print('\n',animal.title(),'would make a great pet.')
print("\n Thease all are farm animals!")