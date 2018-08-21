import screen
screen.clear()

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