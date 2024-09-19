"""
Write a function called make_shirt() that accepts a size and the text of a message that should be
printed on the shirt. The function should print a sentence summarizing the size of the shirt and
the message printed on it.
"""
def make_shirt(size, message):
    print(f"The size of t-shirt is {int(size)}, message will be prited as: {message.capitalize()}")

make_shirt(40, 'this is awesome')

make_shirt(message='this is first', size=42)