from screen import clear
clear()
file_name = 'guest_book.txt'

prompt = '\nPlease select letter on Option Menu:'

select_menu = True

def display_menu():
    print("+- - - - - - - - - - - - - - - -+")
    print("| * * *  GUEST LIST MENU  * * * |")
    print("+- - - - - - - - - - - - - - - -+")
    print('[N]ew Guest')
    print('[D]isplay Guest')
    print('[R]emoved Guest')
    print('[Q]uit Guest Book')
    
def new_guest(file_name):
    clear()
    while True:
        guest = input("Please enter your guest name: ")
        with open(file_name, 'r+') as file_obj:
            guests = file_obj.read()

            if guest.title() in guests:
                print('Guest already exists!')
            elif len(guest.strip()) > 0:
                file_obj.write(guest.title() + "\n")
                print('New guest added to list')
            else:
                print('Invlid input!!!')

        yes_no = input("Do you want to add new guest? [Y]es/[N]o: ")
        if yes_no.upper() == 'N':
            clear()
            display_menu()
            break


display_menu()
while select_menu:
    choices = input(prompt)
    choices = choices.upper()

    if choices == 'N':
        new_guest(file_name)
    elif choices == 'D':
        pass
    elif choices == 'R':
        pass
    elif choices == 'Q':
        clear()
        select_menu = False
    else:
        print("Invalid selection!")
    

    

           
        
     








while select_menu:
    guest = input(prompt)
    with open(file_name, 'a') as file_object:
        file_object.write(guest.title() + "\n")
        print('New guest added to list.')
   
    if guest == '':
        break
