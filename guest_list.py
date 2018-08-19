import os

os.system('clear')

guestlist = ['lorna', 'kathlyn', 'dovvy']

print("Guest List :" + str(guestlist))
# print(guestlist)
print()
for guest in guestlist:
    print("Hi " + guest.title() + "! you are invited for a dinner tomorrow.")

absent_guest = 'dovvy'
guestlist.remove(absent_guest)
print()
print("Sorry... but " + absent_guest.title() + " cannot attend on the dinner tomorrow." )

new_guest = 'daffy'
guestlist.append(new_guest)
print()
for guest in guestlist:
    print("Hi " + guest.title() + "! " + absent_guest.title() + " cannot attend the dinner tomorrow but " + new_guest.title() + " will replaced him.")

# More invited guest
print()
print("Hello everybody, i just found a bigger venue for our dinner. So i inveted more guest, so its fun!!!")
guestlist.insert(0,"Jonny")
guestlist.insert(2, "beverly")
guestlist.insert(-1, "tommy")

print("New guest list:")
for guest in guestlist:
    print("\t" + guest.title())

# Shrinking Guest List
print()
print("Sorry guys but the new dinner table was not arrive and i have only two(2) guest available.")
no_of_guest = len(guestlist) - 2
# i = 0
# print(no_of_guest)
for i in range(no_of_guest):
    # print(i)
    remove_guest = guestlist.pop(0)
    print("Sorry " + remove_guest.title() + ",:-( our dinner was cancelled.")

print()
for guest in guestlist:
    print("\tHello!!!" + guest.title() + " i am waiting for you at our dinner tomorrow.")
print()