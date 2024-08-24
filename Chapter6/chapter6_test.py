
#alien_0 = {'colour':'green'}
#print(f"The alien is {alien_0['colour'].upper()}.")
alien_0 = {'x_pos':0, 'y_pos':25, 'speed':'medium'}
print(f"\nOriginal position is : {alien_0['x_pos']}")
if alien_0['speed'] == 'slow':
    x_increment = 5
elif alien_0['speed'] == 'medium':
    x_increment = 10
else:
    x_increment = 20
# The new position is the old position plus the increment.
alien_0['x_pos'] = alien_0['x_pos'] + x_increment


print(f"\nNew_position : {alien_0['x_pos']}")


"""We first define a dictionary for alien_0 that contains only the alien’s color;
 then we change the value associated with the key 'color'"""
#alien_0['colour'] = 'Yellow'
#print(f"The alien is now {alien_0['colour'].upper()}.")

#alien_0['colour'] = 'green'
#alien_0['points'] = 5
#print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)