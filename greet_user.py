import screen
screen.clear()

def greet_users(names):
    # Print a simple greetings to each user in the list
    for name in names:
        msg = "Hello, " + name.title() + " !"
        print(msg)

usernames = ['daffy', 'mcblood', 'abanz']

greet_users(usernames)