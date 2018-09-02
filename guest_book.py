import time
from screen import clear
clear()
file_name = 'guest_book.txt'


def display_menu():
    # Display menu option selection
    clear()
    print("+- - - - - - - - - - - - - - - -+")
    print("| This is a Guest Book Sample   |")
    print("| * * *  GUEST LIST MENU  * * * |")
    print("+- - - - - - - - - - - - - - - -+")
    print('\n\t[N]ew Guest')
    print('\t[D]isplay Guest')
    print('\t[R]emoved Guest')
    print('\t[E]mpty Guest List')
    print('\t[Q]uit Guest Book')
    
    
def new_guest(file_name):
    # Add new guest to guest_book file
    clear()
    print("<<< Add new guest >>>\n")
    while True:
        guest = input("Please enter your guest name: ")
        if guest == '':
            display_menu()
            break
        else:
            try:
                with open(file_name, 'r+') as file_obj:
                    guests = file_obj.read()

                    if guest in guests:
                        print('Guest already exists!')
                    elif len(guest.strip()) > 0:
                        file_obj.write(guest + "\n")
                        print('New guest added to list')
                    else:
                        print('Invlid input!!!')
            except FileNotFoundError:
                print(f"\nFilename--> '{file_name} ' not found! Please check you data file.\n")
                time.sleep(2)
                display_menu()
                break
            

def display_guests(file_name):
    # Display the list of guest from guest_book file
    seq = 0
    try:
        with open(file_name) as read_file_obj:
            guests_list = read_file_obj.readlines()

            if len(guests_list) == 0:
                print('Guest list is empty!!!')
            else:
                print('<< List of Guests >>')
                guests_list.sort()
                for guest in guests_list:
                    seq += 1
                    print(f'{seq}. {guest.title().rstrip()}')
    except FileNotFoundError:
        print(f"\nFilename--> '{file_name} ' not found! Please check you data file.\n")
            

def remove_guests(file_name):
    clear()
    display_guests(file_name)
    print("\n<< Removed Guest form guestbook >>\n")

    try:
        guest_book = open(file_name)
        guests_list = guest_book.readlines()
        guest_book.close()
    
        name = input("Please enter name of guest to be REMOVED: ")
        name = name+"\n"

        if name in guests_list:
            guests_list.remove(name)

            with open(file_name,'w') as edit_file_obj:
                for guest in guests_list:
                    edit_file_obj.write(guest)
            print(f'{name.strip()} was removed from guest book.')
        else:
            print(f'{name} was not found!')
        
        input("\nPlease any key to back to main menu....")
        display_menu()
    except FileNotFoundError:
        print(f"\nFilename--> '{file_name} ' not found! Please check you data file.\n")

def empty_guests(file_name):
    clear()
    print("<< Guestbook Deletion >>\n")
    yes_no = input('Are you sure you want to ERASE all you guest list[Y]es/[N]? :')
    if yes_no.upper() == 'Y':
        try:
            f = open(file_name, 'w')
            f.write('')
            f.close()
            print("Guest List is now empty!!!")
        except FileNotFoundError:
            print(f"\nFilename--> '{file_name} ' not found! Please check you data file.\n")
    else:
        print("Deletion Cancelled...")

    input("\nPlease any key to back to main menu....")
    display_menu()

def start_up():
    prompt = '\nPlease select letter on Option Menu:'

    select_menu = True
    display_menu()
    while select_menu:
        choices = input(prompt)
        choices = choices.upper()

        if choices == 'N':
            new_guest(file_name)
        elif choices == 'D':
            clear()
            display_guests(file_name)
            input("\nPlease any key to back to main menu....")
            display_menu()
        elif choices == 'R':
            remove_guests(file_name)
        elif choices == "E":
            empty_guests(file_name)
        elif choices == 'Q':
            clear()
            select_menu = False
        else:
            print("Invalid selection!")

if __name__ == '__main__':
    start_up()
