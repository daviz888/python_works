import screen
screen.clear()

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# print("\n")

# Make an empty list for strogin aliens
aliens = []

# Make 30 aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': alien_number, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
print("First five aliens")
for alien in aliens[:5]:
    print(alien)

print("......\n")

# Show how many aliens have been creaated.
print("Total number of aliens: " + str(len(aliens)) + ".\n")