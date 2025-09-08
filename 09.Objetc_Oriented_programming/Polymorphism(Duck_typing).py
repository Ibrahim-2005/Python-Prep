class Animal:
    is_alive=True

class Dog(Animal):
    def sound(self):
        print("BOW BOW!!")

class Cat(Animal):
   def sound(self):
        print("MEOW MEOW!!")


class Car:                              # This is not inherited from animal but it share the same method so it comes under polymorphism
    def sound(self):
        print("HONK HONK!!")

animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.sound()