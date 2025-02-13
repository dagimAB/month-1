



# Create a Vehicle class with attributes make and model.
# Create a class hierarchy Vehicle → Car and Bike.
# Add a subclass Car that includes num_doors and overrides a describe() method.
# Implement methods that highlight polymorphism.
# Ensure encapsulation is used for sensitive attributes.


class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model
    
    def describe(self):
        print("This is a vehicle class!")

class Car(Vehicle):
    def __init__(self,make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors

    def describe(self):
        print(f"Car: {self._make} {self._model}  has {self._num_doors} doors")

class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    
    def describe(self):
        print(f"This bike is {self._make} model {self._model}")


car = Car("Toyota", "Corolla", 4)
bike = Bike("Honda", "CBR")

car.describe()
bike.describe()

