from car import Car, Battery
import screen
screen.clear()

class Electric(Car):
    # Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        # Initialize attributes of the parent class
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        # Electric cars don't have a gas tanks.
        print("This car doesn't need a gas tank!")
    





my_tesla = Electric('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_rage()