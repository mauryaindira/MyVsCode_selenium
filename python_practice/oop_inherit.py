
# function/ method
    
    #problem statement: create an ElectricCar class that inherits the Car class and has additional 
    #attributes battery_size.

from oop_class import Car

class ElectricCar(Car):
    # class contructore
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size= battery_size

mytesla = ElectricCar("tesla", " Model S", "85 kwh")
print(mytesla.brand)
print(mytesla.model)
print(mytesla.fullname())
print(mytesla.battery_size)
