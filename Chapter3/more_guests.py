# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:52:25 2023

@author: vtondlekar
"""

"""You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.

Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.


"""

guest_list = ['guest0', 'guest1', 'guest2']

guest_list.insert(0, 'guest11')
#print(guest_list)

guest_list.insert(2, 'guest21')
#print(guest_list)

guest_list.append('guest33')
#print(guest_list)
print(f"New list is : {guest_list}")

print("\n Honored first name to be invited is:\n",guest_list[0].title())

print(f"\n Honored second name to be invited is:{guest_list[1].title()}")

print(f"\n {guest_list[2].title()}, is third honored invitee")