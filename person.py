import screen
screen.clear()

# Exercises 6.1 Person
employee = {
    'first_name' : 'daffy',
    'last_name' : 'mcblood',
    'age' : 38,
    'city' : 'iligan'
    }

print("Employee Information:")
print("\tFirst Name : " + employee['first_name'].title())
print("\tLast Name  : " + employee['last_name'].title())
print("\tAge        : " + str(employee['age']))
print("\tCity       : " + employee['city'].title())

# Favorite Numbers
print("\nPerson favorite numbers:")

favorite_numbers = {
    'daffy' : 888,
    'ben' : 23,
    'kath' : 21,
    'joy' : 29
}

print(favorite_numbers.items())
print(favorite_numbers.keys())