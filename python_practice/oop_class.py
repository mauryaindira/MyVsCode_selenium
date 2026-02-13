class Car:
    # class contructore
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
    # function/ method
    #problem statement: Add a method to the Car class that displays the fullname
    #of the car(Brand name and model name)

    def fullname(self):
         return f"{self.brand} {self.model}"

# mycar = Car("maruti", " 800")
# print(mycar.brand)
# print(mycar.model)
# print(mycar.fullname())
