dimension = (200, 500)
print(dimension[0])
print(dimension[1])
print()
# Tuple Examples
menu = ('beef afretada', "bulalo", 'fried rice', 'seafood', 'macaronni salad' )

print("Buffet Menu \n============")
for food in menu:
    print("\t" + food.title())

menu = ('sweet n sour pork', 'fish fillet', 'chapsuy', 'plain rice', 'pancit cantoon')
print("\nOur New Menu \n=============")
for food in menu:
    print("\t" + food.title())