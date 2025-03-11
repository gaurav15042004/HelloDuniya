class Car:
    def move(self):
        print("I am a car...Vrooom!")


class Volkswagen(Car):
    def das_auto(self):
        print("das auto!")


class Audi(Car):
    pass


car1=Volkswagen()
car1.move()
car1.das_auto()