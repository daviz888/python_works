pizzas = ['hawaian', 'pepperoni', 'ham and cheese', 'vegetable', 'chicken adobo']
friend_pizzas = pizzas[:]
pizzas.append('beef special')
friend_pizzas.append('bacon & cheese')

print("My favorite pizza are: ")
for pizza in pizzas:
    print("\t" +pizza.title())

print("\nMy friend favorite pizza are:")
for friend_pizza in friend_pizzas:
    print("\t" + friend_pizza.title())