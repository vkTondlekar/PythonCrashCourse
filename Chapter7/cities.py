"""
consider a program that asks the user about places they’ve visited.
Break the loop as soon as the user enters the 'quit' value.
"""
prompt = "\n Please enter the name of the cities you have visited!: "
prompt += "\n Enter 'quit' when you are finished."

while True:
    city = input(prompt.casefold())
#print(city)
    if city.casefold() == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()} for vacation!")