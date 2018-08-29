from screen import clear
clear()

file_name = 'guest.txt'

prompt = 'Please enter guest name :'

while True:
    guest = input(prompt)
    with open(file_name, 'a') as file_object:
        file_object.write(guest.title() + "\n")
        print('New guest added to list.')
   
    if guest == '':
        break
