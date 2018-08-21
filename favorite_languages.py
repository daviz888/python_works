import screen
screen.clear()

favorite_languages = {
    'jen': ['python', 'pascal', 'basic'],
    'sarah': ['c', 'c++', 'c#', 'visual basic'],
    'edward': ['ruby', 'perl', 'swift', 'python'],
    'phil': ['python', 'php', 'java'],
    'dovvy': ['C#', 'foxpro', 'swift', 'ms access', 'visual basic']
    }

print("Sarah's favorite programming language are: " + 
    str(favorite_languages['sarah']) + ".")

print("\nLooping keys & value in dictinaires:\n")
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language(s) are:")
    for language in languages:
        print("\t" + language.title())

print("\nLooping through all keys in dictionary\n")

for name in favorite_languages.keys():
    print(name.title())

print("\nAnother examples:\n")

friends = ['phil', 'sarah']

for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("-->Hi " + name.title() + 
            ", I see your favorite programming language are: ")
        for language in favorite_languages[name]:
            print("\t" + language.title())

print("\n")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through a Dictionary's Keys in Order
print("Looping through a Dictionary's Keys in Order.\n")

for favorite_language in sorted(favorite_languages.keys()):
    print(favorite_language.title() + ", thank you for taking the poll.")

print("\nLooping through all Values in a Dictionary")
print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language)