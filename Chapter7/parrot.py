"""
program asks the user to enter some text, then displays that message back to the user
"""
#from Chapter7.rental_car import prompt

"""
message = input(" Tell me something, and I will repeat it back to you: ")

print("\t",message)

name = input("\n What is your name? ")
print(f"\n Hello {name.title()}! how are you doing?")
"""

prompts = "\nTell me something, and I will repeat it back to you."
prompts += "\nEnter 'quit' to end program."

message = ""
while message.casefold() != 'quit':
    message = input(prompts)

    if message.casefold() != 'quit':
        print(message)
