import screen
screen.clear()

# Dictionary examples
print("Dictionary examples:\n====================")
alien_0 = {'color': 'green', 'points': 5}
print("Alien info:")
print("\tColor : " + alien_0['color'].title())
print(f"\tPoints:  {alien_0['points']}")

print("\nAlien Shootdown!!!")
new_points = alien_0['points']

print(f'\nYou just earned {new_points} points!')

# add new pair keys to Dictionary
print("\nAdd alien coordinates x,y position")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Start with empty Dictionary
alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 8
print("\nAlein 1 information:")
print(alien_1)

# Modifiying values in Dictionary
print("\nModifiying alien dictionary:")
alien_0['speed'] = 'medium'
print("Alein coordinate position:")
print(f"\tX coordinate : {alien_0['x_position']}")
print(f"\tY coordinate : {alien_0['y_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"\nNew x-position: {alien_0['x_position']}")

# Removing Key-Value Pairs in Dictionary
print("\nRemoving alien points:")
del alien_0['points']
print(alien_0)