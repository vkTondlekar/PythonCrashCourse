# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 21:58:34 2023

@author: vtondlekar

Think of at least five places in the world you’d like to visit.

Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list 
neatly; just print it as a raw Python list.

"""

places =['norway', 'switzerland', 'chile', 'africa', 'japan']

print("Favourite places list is:")
print(places)

#Use sorted() to print your list in alphabetical order without modifying the
#actual list.

print("\nSorted list is:")
print(sorted(places))

#Show that your list is still in its original order by printing it.
print("\nOriginal list is:")
print(places)

#Use sorted() to print your list in reverse-alphabetical order without 
#changing the order of the original list.
print("\n",sorted(places, reverse=True))

#Show that your list is still in its original order by printing it again.
print("\nOriginal list is:")
print(places)

#Use reverse() to change the order of your list. Print the list to show that 
#its order has changed
places.reverse()
print("\n",places)

#Use reverse() to change the order of your list again. Print the list to show 
#it’s back to its original order
places.reverse()
print("\n",places)

#Use sort() to change your list so it’s stored in alphabetical order. 
#Print the list to show that its order has been changed.
places.sort()
print("\n",places)

#Use sort() to change your list so it’s stored in reverse-alphabetical order. 
#Print the list to show that its order has changed.
places.sort(reverse=True)
print("\n",places)

