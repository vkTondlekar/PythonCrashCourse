"""
A more realistic example would involve more than three aliens with code that automatically generates each alien.
In the following example, we use range() to create a fleet of 30 aliens:
"""
# make an empty list for storing aliens.

aliens = []
# This example begins with an empty list to hold all the aliens that will be created.

# make 30 green aliens.

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# The range() function returns a series of numbers, which just tells Python how many times we want the loop to repeat.
# Each time the loop runs, we create a new alien
# and then append each new alien to the list aliens

# show the first 5 aliens.

for alien in aliens[:5]:
    print(alien)
print("End...")
# We use a slice to print the first five aliens

# show me how many aliens created

print(f"Total number of aliens {len(aliens)}")

# and finally, we print the length of the list to prove we’ve actually generated the full fleet of 30 aliens
