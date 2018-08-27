import string
import screen

screen.clear()

file_name ='learning_python.txt'

with open(file_name) as file_object:
    print("Read contents:\n=================")
    contents = file_object.read()
    print(contents)


with open(file_name) as file_object1:
    print("\nRead lines:\n=============")

    for line in file_object1.readlines():
        print(line.rstrip())


print("\nString Lines\n=================")
with open(file_name) as file_object2:
    lines = file_object2.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  

print(pi_string.replace('Python', 'C'))
print(len(pi_string))

print("\nUsing replace() method:\n==================")
message = "I really like dogs."

print(message.replace('dog', 'cat'))