from car import Car

class Battery():
    """Modeling the battery of an electric car"""
    def __init__(self,battery_size=75):
        """setting the attributes of the battery"""
        self.battery_size = battery_size

    def describe_battery(self):
        """prints out the size of the battery"""
        print(f"This car has a {self.battery_size} KW battery")

    def get_range(self):
        """prints out the range the car can travel"""
        if self.battery_size == 75:
            range = 360
        if self.battery_size == 100:
            range = 540
        print(f"This car can go {range} miles" )

class ElectricCar(Car):
    """An attempt to model an electric car from an existing car"""
    def __init__(self,make,model,year):
        """inheriting all the atrribute and methods of the parent class
            and setting additional attributes"""
        super().__init__(make,model,year)
        self.battery = Battery()


    def refuel_tank(self):
        """removing fuel tank from an electric car"""
        print(f"{self.make} doesn't have a fuel tank")

# i am adding a dummy text
