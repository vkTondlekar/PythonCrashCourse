

responses = {}

polling_active = True

while polling_active:
    name = input("\n What is your good name?\n")
    response = input("\n Which mountain you would like to climb? ")

    responses[name] = response

    repeat = input("\n Would you like to give another try? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("----Poll results----")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")

    