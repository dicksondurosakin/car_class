class Car():
    """An attempt to model a car"""
    def __init__(self,make,model,year):
        """Attributes of the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """describes the full name of the car"""
        return f"{self.year} {self.make} {self.model}"

    def update_odometer(self,mileage):
        """Reject mileage if its lesser than odometer reading or 
            change the value on the odometer reading"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer backward")
    
    def increment_odometer(self,miles):
        """increases the value on the odometer"""
        self.odometer_reading += miles

    def read_odometer(self):
        """prints out the reading on the odometer"""
        print(f"This car has travelled {self.odometer_reading} miles")

    def refuel_tank(self):
        """refuels the car"""
        print(f"{self.make} is currently refueling")
