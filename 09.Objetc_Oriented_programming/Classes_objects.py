class Car:
    no_of_cars=0        # Class variable
    def __init__(self,company,manufactured_year,color):     #Constructor
        self.company=company
        self.manufactured_year=manufactured_year
        self.color=color
        self.is_working=True
        Car.no_of_cars+=1

    def __str__(self):
        return f"The car name is {self.company} which is manufactured in {self.manufactured_year} and it is {self.color} in colour"
    
    def car_condition(self):
        print(f"{self.company} is working" if self.is_working else f"{self.company} is not working")
    
    def change_car_condition(self,condition):
        self.is_working=condition


    
car1=Car("AUDI",2023,"Red")
print(car1)
confirmation=input("Do you wanna change the condition of the car?(Y/N):")
if confirmation.lower()=="y":
    condition=input("Is car working(Y/N):")
    car1.change_car_condition(True if condition.lower()=="y" else False)
car1.car_condition()
print(Car.no_of_cars)