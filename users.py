import screen
screen.clear()

# Looping dictionaries
print("Looping Dictionaries\n")
users_0 = {
    'username': 'efemi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in users_0.items():
    print("\nKey: " + key)
    print("Valeu: " + value)