import screen
screen.clear()

# Ordeinal Numbers example
print("Ordinal Numbers :")
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for value in ordinal_numbers:
    if value == 1:
        print(f'\n\t {value}st')
    elif value == 2:
        print(f'\n\t {value}nd')
    elif value == 3:
        print(f'\n\t {value}rd')
    else:
        print(f'\n\t {value}th')

print("\n\n")