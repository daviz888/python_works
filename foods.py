my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite fodds are:")
for myfood in my_foods:
    print("\t" + myfood.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print("\t" + friend_food.title())

print()
print("Version 2" + "\n=========")

fav_foods = ['pizza', 'falafel', 'banna cake']
my_friend_fav_food = fav_foods

fav_foods.append('adobo')
my_friend_fav_food.append('letson')

print("My favorite foods are:")
for fav_food in fav_foods:
    print("\t" +fav_food.title())

print("\nMy Friends favorite foods are:")
for friend_fav_food in my_friend_fav_food:
    print("\t" + friend_fav_food.title())