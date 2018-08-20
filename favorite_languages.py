import screen
screen.clear()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rubt',
    'phil': 'python'
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