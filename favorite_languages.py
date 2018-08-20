import screen
screen.clear()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'dovvy': 'C#'
    }

print("Sarah's favorite programming language is " + 
    favorite_languages['sarah'].title() +
    ".")

print("\nLooping keys & value in dictinaires:\n")
for name, language in favorite_languages.items():
    print(name.title() +"'s favorite language is " +
        language.title() + ".")

print("\nLooping through all keys in dictionary\n")

for name in favorite_languages.keys():
    print(name.title())

print("\nAnother examples:\n")

friends = ['phil', 'sarah']

for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("\tHi " + name.title() + 
            ", I see your favorite programming language is " +
            favorite_languages[name].title() + "!")

print("\n")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through a Dictionary's Keys in Order
print("Looping through a Dictionary's Keys in Order.\n")

for favorite_language in sorted(favorite_languages.keys()):
    print(favorite_language.title() + ", thank you for taking the poll.")

print("\nLooping through all Values in a Dictionary")
print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print("\t" + language.title())