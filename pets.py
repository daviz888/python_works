import screen
screen.clear()
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("Currents list of pets:")
print(f' {pets} \n')

while 'cat' in pets:
    pets.remove('cat')

print("List of pets after removal:")
print(f'{pets}\n')
