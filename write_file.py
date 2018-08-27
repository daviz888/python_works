import screen
screen.clear()

file_name = 'my_file.txt'

message = input("Please write your message to save to file: ")

with open(file_name, 'w') as file_object:
    file_object.write(message)
    print('message save to file.')