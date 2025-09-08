class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power

class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self,name,model,horse_power,wheel_size):
        self.name=name
        self.model=model
        self.engine=Engine(horse_power)
        self.wheel_size=[Wheel(wheel_size) for _ in range(4)]
    
    def car_details(self):
        print(f"It is a {self.name} {self.model} with a ")
