"""
Write a program that asks the user how many people are in their dinner group. If the answer is more than eight,
print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
"""
question = input(f"How many people are in your dinner group? \n")

question = int(question)

if question > 8:
    print("Kindly wait while another table to available.")
else:
    print("\nPlease have seat at table number 4.")