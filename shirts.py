import screen
screen.clear()

# //Exercise 8.2 T-Shirt examples

print("*---- T-Shirt Print ----*")

accepts = True

def make_shirt(size, print_out):
    print("\tYour T-shirt size is: " + t_shirt_size + ".")
    print("\tWith prints of      : " + t_shirt_print.upper() + "!")


while accepts:
    t_shirt_size = input("\nPlease enter your T-shirt Size [L]-arge/[M]edium/[S]mall: ")
    t_shirt_print = input("\nEnter the text to be printed on your T-shirt: ")
    make_shirt(t_shirt_size, t_shirt_print)

    prompt = "\nWould you like to make another T-Shirts? Y/N :"
    yes_no = input(prompt)
    if yes_no.upper() == 'N':
        accepts = False

