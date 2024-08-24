# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:24:26 2023

@author: vtondlekar
"""

"""You just heard that one of your guests can’t make the dinner,
so you need to send out a new set of invitations. You’ll have to
think of someone else to invite."""

guest_list = ['guest0', 'guest1', 'guest2']

print("\n Honored first name to be invited is:\n",guest_list[0].title())

print(f"\n Honored second name to be invited is:{guest_list[1].title()}")

print(f"\n {guest_list[2].title()}, is third honored invitee")

#del guest_list[1]

guest_list_temp = guest_list.pop(1)

print(f"\n {guest_list_temp.title()} won't make it to dinner")

#print("\n Temporary guest list looks like this:\n",guest_list)

guest_list.insert(1,'guest6')

#print("\n New Guest list would look like this:\n",guest_list)
print(f"\n New invitee is {guest_list[1].title()}, in place of {guest_list_temp.title()}")

#print(guest_list)
