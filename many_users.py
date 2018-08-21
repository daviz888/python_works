import screen
screen.clear()

# Looping dictionaries
print("Looping through Dictionaries with in the dictionaries:\n")
users = {
    'admin': {
        'first': 'daffy',
        'last': 'dack',
        'location': 'philippines'
        },
    'guest': {
        'first': 'viron',
        'last': 'alien',
        'location': 'mars' 
        }
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print(f'\tFull Name: {full_name.title()} ')
    print(f'\tLocation : {location.title()} ')