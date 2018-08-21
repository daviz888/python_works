import screen
screen.clear()

# Exercises 6.7 People
person_0 = {
    'first_name' : 'daffy',
    'last_name' : 'mcblood',
    'age' : 38,
    'city' : 'iligan'
    }

person_1 = {
    'first_name': 'jane',
    'last_name': 'joe',
    'age': 28,
    'city': 'hawai'
    }

person_2 = {
    'first_name': 'joy',
    'last_name': 'abanz',
    'age': 19,
    'city': 'manila'
    }

people = [person_0, person_1, person_2]

cnt = 1

print("List of People Information:")
for person in people:
    print(f'\nPerson {cnt}:\n--------- ')
    cnt +=1
    for key, value in person.items():
        print(f'\t{key.title()} : {value} ')
