# Abstraction Example
# We hide the details of how the car starts from the user.

class Car:
    def __init__(self):
        self.is_started = False
        self.brake = False
        self.clutch = False
    
    # This method hides the steps of starting a car
    def start_car(self):
        self.is_started = True
        self.clutch = True
        print("Car Started...")

# User just calls start_car(), no need to know the steps
Car1 = Car()
Car1.start_car()
