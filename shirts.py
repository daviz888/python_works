import screen
screen.clear()

# //Exercise 8.2 T-Shirt examples
accepts = True


sizes = {
    'XL': 'extra large',
    'L': 'large',
    'M': 'medium',
    'S': 'small'
}

def display_menu():
    print("==== T-Shirt Printing ===")
    print("====  SELECTION MENU  ===\n")
    print("Chosee you size")
    # loop dictionary for menu selection
    
    for key, value in sizes.items():
        print("\t" + key + "- " + value.title())

def make_shirt(shirt_text, shirt_size = 'L'):
    if shirt_size in sizes:
        size = sizes[shirt_size]
    else:
        size = 'Cannot determine the size'
    print("\tYour T-shirt size is: " + size.upper() + ".")
    print("\tWith prints of      : " + shirt_text.upper())

while accepts:
    display_menu()
    shirt_size = input( "\t_")

    if shirt_size.upper() in sizes:
        shirt_text = input("\nEnter the text to be printed on your T-shirt: ")
        make_shirt(shirt_text)

        prompt = "\nWould you like to make another T-Shirts? Y/N :"
        yes_no = input(prompt)
        if yes_no.upper() == 'N':
            accepts = False
        screen.clear()
    else:
        print("Invalid size please select from the selection menu!\n")    
   

   

