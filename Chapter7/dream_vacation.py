"""
Write a program that polls users about their dream vacation. Write a prompt similar to If you could
visit one place in the world, where would you go? Include a block of code that prints the results of
the poll.
"""


responses = {}
polling = True
while polling:
    name = input("What is your name?  ")
    response = input("If you could visit one place in the world, where would you go?\n")
    responses[name] = response

    repeat = input("Any other place?")
    if repeat.casefold() == 'no':
        break
print("<<<<< Poll results >>>>>")
for name, response in responses.items():
    print(f"{name.title()} loves to go on dream vacation at {response.title()}.")