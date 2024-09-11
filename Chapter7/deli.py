"""
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make
an empty list called finished_sandwiches. Loop through the list of sandwich orders and print
a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it
to the list of finished sandwiches. After all the sandwiches have been made, print a message
listing each sandwich that was made.
"""
sandwich_orders = ['tuna', 'chicken', 'paneer', 'prawn', 'veg']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I have made your {current_sandwich.title()} sandwich, enjoy!")
    finished_sandwiches.append(current_sandwich)
#sort

print(f"\n******* Finished sandwich orders *******")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
