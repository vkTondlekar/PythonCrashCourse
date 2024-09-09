"""
program asks the user to enter some text, then displays that message back to the user.
use flag
"""
prompt = input(" Tell me something, and I will repeat it back to you: ")

prompt += "\nEnter 'quit' to end the program. "

#We set the variable active to True so the program starts in an active state.
#As long as the active variable remains True, the loop will continue running
active = True

while active:
    message = input(prompt)
#In the if statement inside the while loop, we check the value of message once the user enters their input
    if message.casefold() == "quit":
#If the user enters 'quit', we set active to False, and the while loop stops.
        active = False
    else:
#If the user enters anything other than 'quit', we print their input as a message.
        print(message)