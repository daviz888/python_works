import screen
screen.clear()

def make_car(manufacturer, model, **parts):
    car_info = {}
    car_info['manufactured'] = manufacturer
    car_info['model'] = model
    for key, value in parts.items():
        car_info[key] = value

    return car_info

car = make_car('Toyota', 'enova',
                color='whote',
                year= 2018,
                insured=True,
                monthly=3000)

for key, value in car.items():
    print(f'{key.title()} : {value} ')