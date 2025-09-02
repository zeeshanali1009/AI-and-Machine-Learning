# abstraction is used for hiding compex things from the general users 

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(vehicle):
    def start(self):
        print(f"Car starts with the key.")

class Bike(vehicle):
    def start(self):
        print(f"Bike starts with the button.")    

car =  Car()
bike = Bike()

car.start()
bike.start()
