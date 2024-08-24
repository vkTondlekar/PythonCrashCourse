# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:51:16 2023

@author: vtondlekar
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

numbers = list(range(2,11,2))
print('\n',numbers)

squares=[]
for i in range(1,11):
    #square = i ** 2
    squares.append(i**2)
print('\n',squares)

digits=[1,2,3,4,5]
print('\n',min(digits))
print('\n',max(digits))
print('\n',sum(digits))