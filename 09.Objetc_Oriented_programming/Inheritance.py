class Organisms():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.is_living=True

    def details(self):
        print(f"{self.name} is {self.age} years old and is {'alive' if self.is_living else 'dead'}")

    def move(self):
        print(f"{self.name} {'moves' if self.is_living else 'is dead'}")


class Bait(Organisms):
    def is_bait(self):
        print(f"{self.name} can be used as bait")
    

class Hunter(Organisms):
    def does_hunt(self):
        print(f"{self.name} can hunt")

class Lion(Hunter):
    def hunts(self,hunts_who):
        print(f"{self.name} hunts {hunts_who.name}")
        hunts_who.is_living = False


class Human(Bait,Hunter):
    pass

bob=Human("Afza",20)
bob.details()
bob.move()
bob.is_bait()
bob.does_hunt()

mufasa=Lion("Ibbu",30)
mufasa.hunts(bob)

# bob.details()