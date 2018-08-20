import screen

screen.clear()

glossary = {
    'boolean': 'data types eathier True or False',
    'dictionary': 'is a collection of key-value pairs',
    'tuple': 'is an immutable list',
    'list': 'is colletion of items in a particular order',
    'range': 'is python function that generate a series of numbers',
    'print': 'python command for output to the screen',
    'ifelifelse': 'conditional statements in python',
    'string': ' data types to store string values or charaters'
    }

print("Glossary exercise using Ditionary:\n==================================\n")
sequence = 0
for key, value in glossary.items():
    sequence += 1
    print(str(sequence)+". " + key.title() + " - " + value.capitalize() + ".\n")