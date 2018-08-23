import screen
screen.clear()


def make_pizza(size, *toppings):
    # print the list of toppings that have been requested.
    # Summarize the pizza we are about to make.
    print(f'\nMaking a {size} inch pizza with the following toppings: ')
    for topping in toppings:
        print("- " + topping)


# Store information about a pizza being ordered
cnt = 0
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
    }

# summarize the order.
print("You ordered a " + pizza['crust'] + "-crust puzza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    cnt += 1
    print("\t" +str(cnt) +"-" + topping)

print("\nPassing an Arbitiary Number of Arguments Example in function:")
print("=============================================================")

make_pizza(16, "pepperoni")
make_pizza(20, 'mushrooms', 'green peppers', 'pineapple', 'extra cheese')