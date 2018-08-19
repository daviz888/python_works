import screen
screen.clear()

username = 'admin'
users = ['daffy', 'jhon', 'mike', 'admin', 'aban']

if users:
    print("Login Users:")
    for user in users:
        if user == username:
            print("\n\tWelcome " + user.title() + ", would you like to see the report?")
        else:
            print("\n\tWelcome " + user.title() + " thank you for logging in again." )
else:
    print("We need to find some users!")
    
print("\n")