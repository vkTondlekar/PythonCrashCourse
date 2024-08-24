""" Write a series of conditional tests. Print a statement describing each test and your
 prediction for the results of each test. Your code should look something like this
"""
from typing import List

# Tests for equality and inequality with strings

name_1: str = "John"
name_2: str = "Johny"
name_3: str = "John"


print(name_1 == name_3)

print(name_1 == name_2)

print(name_1 != name_2)

# Tests using the lower() method

print('\n',name_1.lower() == "john")

"""Numerical tests involving equality and inequality  greater than and less than, greater than or equal to, and 
less than or equal to"""

number = 13

print(number < 13)
print(number <= 13)
print(number > 13)

# Tests using the and keyword and the or keyword

print('\n or operator is:',number < 14 or number == 14)

print('\n and operator is:', number < 14 and number ==14)

# Test whether an item is in a list

names = ['john', 'johny', 'janardan']

print('\n','john' in names)

# Test whether an item is not in a list

print('\n','jonty' in names)