"""
Modify the make_shirt() function so that shirts are large by default with a message that reads
I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of
any size with a different message.
"""


def large_shirt(size, message='I love python'):
    print(f"The size of t-shirt is {int(size)}, message will be prited as: {message.capitalize()}")


large_shirt(40)