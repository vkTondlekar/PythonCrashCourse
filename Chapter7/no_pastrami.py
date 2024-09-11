"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list
at least three times. Add code near the beginning of your program to print a message saying the deli
has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from
sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""
#from Chapter7.deli import finished_sandwiches

sandwich_orders = ['tuna', 'pastrami','chicken', 'pastrami', 'paneer', 'prawn', 'veg','pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)

while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')
print(finished_sandwiches)