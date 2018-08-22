import screen
screen.clear()
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("Currents list of pets:")
print(f' {pets} \n')

def remove_pets(pet_name):
    while pet_name in pets:
        pets.remove(pet_name)

remove_pets(pet_name = 'cat')

print("List of pets after removal:")
print(f'{pets}\n')
