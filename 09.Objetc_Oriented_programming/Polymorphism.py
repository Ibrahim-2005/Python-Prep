class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (self.radius*self.radius*3.14)

class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        return (self.side**2)

class Triangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return ((self.height*self.width)*1/2)

class Pizza(Circle):                    # Polymorphism by inheritance
    def __init__(self, radius,topping):
        super().__init__(radius)
        self.topping=topping
    
shapes=[Circle(5),Square(6),Triangle(7,8),Pizza(5,"Pineapple")]

for shape in shapes:
    print(f"{shape.area()} cm ²")

