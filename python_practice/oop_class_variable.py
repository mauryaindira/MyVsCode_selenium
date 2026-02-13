class Car:

    total_car=0

    def __init__(self, brandname , model):
        self.brandname= brandname
        self.model=model
        Car.total_car =+ 1

    def showyourcar(self):
        print( self.brandname , self.model )
    
    def fueltype(self):
        return "Disel and Petrol"
    
    @staticmethod
    def general_description():
        return "Cars are means of transportaion"

class Electriccar:

    def __init__(self, brandname , model):
        self.brandname= brandname
        self.model=model
     # Instance Method
    def showyourcar(self):
        print( self.brandname , self.model )
    
    def fueltype(self):
        return "Electric Car"
    

mycar= Car("Maruti", "800cc") 
  
print(mycar.general_description())

#mycar1= Electriccar("Tesla", "eve")
# print(mycar1.fueltype())

# obj1= Car("Tata", "Safari")
# print(obj1.general_description())

#creates an object (self = that object)
#general_description(self) is called with access to instance attributes (brand, model).
#print("General calling....",Car("Tata", "Safari").general_description()) 
print(Car.general_description()) #Class Method Call (without an object);
# it will Not work (unless general_description() made @classmethod or @staticmethod)

#print("Object level calling", obj1.general_description())

print(Car.total_car)


        
        