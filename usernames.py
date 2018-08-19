import screen
screen.clear()

# Check Username
current_users = ['daffy', 'jhon', 'mike', 'admin', 'john']
new_users = ['admin', 'daffy', 'kathlyn', 'lorna']

# convert element in the list to upper case
current_users =[element.upper() for element in current_users]

print("Username Exerise\n==============\n")

for user in new_users:
    if user.upper() in current_users:
        print("\nSorry " + user.title() + " is already exist!, Please select another one.")
    else:
        print("\nUsername " + user.title() + " is available!")

print()