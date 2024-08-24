# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:16:16 2023

@author: vtondlekar
"""
""" You just found out that your new dinner table won’t arrive in time for the 
dinner, and now you have space for only two guests.

Start with your program from Exercise 3-6. Add a new line that prints a message
saying that you can invite only two people for dinner.
 
Use pop() to remove guests from your list one at a time until only two names 
remain in your list. Each time you pop a name from your list, print a message 
to that person letting them know you’re sorry you can’t invite them to dinner.

Print a message to each of the two people still on your list, letting them 
know they’re still invited.

Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of 
your program.


"""
guest_list = ['guest11','guest0', 'guest21', 'guest1', 'guest2','guest31']

#print(guest_list)
print("\n I can invite only two people, Apologies for incovinience!")

removed_guest_list = guest_list.pop()

removed_guest_list = guest_list.pop()

removed_guest_list = guest_list.pop()

removed_guest_list = guest_list.pop()
#print(removed_guest_list)
#print(guest_list)

print(f"\n{guest_list[0].title()}, you are still invited.")

print(f"You are also on list, {guest_list[1].title()} !")

del guest_list[0]
del guest_list[0]
print("\nLooks like empty list:",guest_list)