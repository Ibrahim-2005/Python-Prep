from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def accelerator(self):
        pass

    @abstractmethod
    def brake(self):
        pass

class Car(Vehicle):
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def accelerator(self):
        print(f"{self.name} goes.")

    def brake(self):
        print(f"{self.name} stops.")

car1=Car("Ferrari","Red")
car1.accelerator()
car1.brake()