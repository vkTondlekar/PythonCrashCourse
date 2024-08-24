# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:36:15 2023

@author: vtondlekar
"""
"""Think of things you could store in a list. For example, you could make 
a list of mountains, rivers, countries, cities, languages, or anything 
else you’d like. Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once.
"""


mylist = ["norway", "japan", "germany", "sweden", "switzerland"]

print("\n Original list is:\n",mylist)
#append
mylist.append("Ireland")

print("\n Appended list is:\n",mylist)

#insert
mylist.insert(2,"Denmark")
print("\n Inserted list is:\n",mylist)

#sorted
mylist_sorted = sorted(mylist)
print("\n sorted list is :\n",mylist_sorted)
print("\n",mylist)


#sorted reverse
mylist_sorted = sorted(mylist, reverse=True)
print("\n reverse sorted list is:\n",mylist_sorted)

#reverse
mylist.reverse()
print("\n reversed list is:\n",mylist)

#del
del mylist[2]
print("\n",mylist)

#pop
popped_mylist = mylist.pop()
print("\n popped item is:\n",popped_mylist)
print("\n",mylist)

#remove 
#The remove() method deletes only the first occurrence of the value you specify.
mylist.remove("germany")
print("\n",mylist)
#sort
mylist.sort()
print("\n",mylist)

#sort reverse
mylist.sort(reverse=True)
print("\n",mylist)

#len
print("\n length os mylist is: ",len(mylist))
