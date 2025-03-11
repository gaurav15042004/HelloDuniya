class Person():
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
    def talk(self):
        print(f"Hello I am {self.name} {self.surname} and I am {self.age} years old")


Person("Gaurav", "Sharma", 20).talk()

Person("John", "Smith", 20).talk()
