# Working with Class examples

# import screen
# screen.clear()

class Car():
    # A simple attempt to represent a car
    def __init__(self, make, model, year):
        # Initialize attroibutes to describe a car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name.
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # Print a statement showing the car's mileage'
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # Set the odometer reading to the given value.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        # Add the given amount to the odometer reading
        self.odometer_reading += mileage

    def fill_gas_tank(self, liters):
        # Fill car with gasoline
        self.gas += liters

class Battery():
    # A simple attempt to model a battery for an electric car.
    def __init__(self, battery_size=70):
        # Initialize the battery attributes
        self.battery_size = battery_size

    def describe_battery(self):
        # Print a statement that describe the battery size.
        print("This car has a "+ str(self.battery_size) + "-kWH battery.")

    def get_rage(self):
        # Print a statement about the range this battery provides.
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximetly " + str(range)
        message += " miles on a full charge."
        print(message)