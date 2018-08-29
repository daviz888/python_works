from screen import clear

clear()
file_name = 'my_file.txt'

while True: 
    message = input("Please Enter your message:")
    with open(file_name, 'a') as file_object:
        file_object.write(message + "\n")

    yes_no = input("\nDo you want to write new message? [N/Y] :")
    if yes_no.upper() == 'N':
        break

clear()
print("Display Messages:\n")

with open('file_name') as file_obj:
    lines = file_obj.readlines()
    for line in lines:
        print(line)