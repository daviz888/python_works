import screen

screen.clear()

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print("\nFinished making your pizza!")
print("\n\nTopping Version 2 \n=================\n")

most_requested_toppings = []

if most_requested_toppings:
    for most_requested_topping in most_requested_toppings:
        print("Adding " + most_requested_topping + ".")
else:
    print("Are you sure you want your pizza?")

print("\n\nTopping Version 3 \n=================\n")

avialable_toppings = ['mushroom', 'olives', 'green peppers', 
                      'pepproroni', 'pineapple', 'extra cheese']

requestedToppings = ['mushroom', 'french fries', 'extra cheese']

for requestedTopping in requestedToppings:
    if requestedTopping in avialable_toppings:
        print("\tAdding " + requestedTopping +".")
    else:
        print("\tSorry, we don't have " + requestedTopping + ".")
print("\nFinished making your pizza!")