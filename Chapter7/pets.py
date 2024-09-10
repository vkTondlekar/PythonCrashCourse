"""
Say you have a list of pets with the value 'cat' repeated several times. To remove all instances of
that value, you can run a while loop until 'cat' is no longer in the list
"""
pets = ['dog', 'cat', 'rabbit', 'turtle', 'cat', 'parrot', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print("\n",pets)

