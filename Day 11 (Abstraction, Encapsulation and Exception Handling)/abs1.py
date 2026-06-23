from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is started using Key")

class Bike(Vehicle):
    def start(self):
        print("Bike started using Kick")

bmw = Car()
bmw.start()

apache = Bike()
apache.start()
