"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""
#from Chapter7.parrot_flag import active

prompt = "\nEnter the topping which you like: "
prompt += "\nEnter 'quit' when have enough toppings! \n"

while True:
    toppings = input(prompt)
    if toppings.casefold() == 'quit':
        break
    else:
        print(f"\tI will add {toppings.title()} toppings to your pizza! ")

