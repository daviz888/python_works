motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

last_owned = motorcycles.pop(1)

print("The last motorcycle I owned was a " + last_owned.title() + ".")

cars = ['Hyundai', 'toyota', 'Nissan', 'ford', 'gmc']

cars.remove('gmc')

print(cars)

print("list example 2")

high_end_cars = ['ferrari', 'dodge', 'audi', 'bmw', 'mercides']

too_expensive = 'ferrari'
high_end_cars.remove(too_expensive)

print(high_end_cars)

print("\nA " + too_expensive.title() + " is to expensive for me.")

