"""
Make a list of your favorite fruits, and then write a series of independent if statements that
check for certain fruits in your list.
Make a list of your three favorite fruits and call it favorite_fruits.
Write five if statements. Each should check whether a certain kind of fruit is in your list.
If the fruit is in your list, the if block should print a statement, such as You really like bananas!
"""
favourite_fruits = ['banana', 'orange', 'mango', 'grapes', 'watermelon']

if 'banana' in favourite_fruits:
    print(f"I really like,{favourite_fruits[0].title()}")
if 'orange' in favourite_fruits:
    print(f"I really like,{favourite_fruits[1].title()}!")
if 'mango' in favourite_fruits:
    print(f"I really like,{favourite_fruits[2].title()}.")
if 'grapes' in favourite_fruits:
    print(f"I really like,{favourite_fruits[3].title()}!")
if 'watermelon' in favourite_fruits:
    print(f"I really like,{favourite_fruits[4].title()}.")
