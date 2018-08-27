import screen
screen.clear()

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input("Please enter your birthday in [mmddyy] format: ")
if birthday in pi_string:
    print('Your birthdat appears in digit pi!')
else:
    print('Your birthday does not appear in digit pi!')


print(pi_string)
print(len(pi_string))

