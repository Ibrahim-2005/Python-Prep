
class Shape():
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    
    def describe(self):
        print(f"It is {self.color} in color and it is {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        super().__init__(color, is_filled)
        self.radius=radius
    def describe(self):
        print(f"It is a circle and the area of the circle is {self.radius*self.radius*3.14}")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled,side):
        super().__init__(color, is_filled)
        self.side=side
    def describe(self):
        print(f"It is a square and the area of the square is {self.side*4}²")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled,height,width):
        super().__init__(color, is_filled)
        self.height=height
        self.width=width
    def describe(self):
        print(f"It is a triangle and the area of the triangle is {1/2*self.height*self.width}")
        super().describe()

cir=Circle("Red",True,5)
cir.describe()

sq=Square("Blue",False,8)
sq.describe()

tri=Triangle("Green",True,1,7)
tri.describe()