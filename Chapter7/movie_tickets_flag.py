"""
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3,
the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
Use flag
"""

message1 = "\nEnter age in positive integer:\n"
message1 += "\nEnter to quit when done booking tickets!\n"

active = True
while active:
    age = input(message1)
    if age.casefold() == 'quit':
        active = False

    age = int(age)

    if age < 3:
        print("You go free for movie, enjoy!")
    elif age < 13:
        print("Your ticket is 10$.")
    else:
        print("Your ticket is 15$.")
