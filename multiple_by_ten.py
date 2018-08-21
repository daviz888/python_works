import screen
screen.clear()

number_input = input("Please enter a number :")

check_no = int(number_input)

if check_no % 10 == 0:
    print("\nThe "+ str(check_no) + " is multiple by ten.")
else:
    print("\nThe " + str(check_no) + " is NOT multiple by ten.")