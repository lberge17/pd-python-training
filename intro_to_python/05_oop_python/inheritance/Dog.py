from Animal import Animal;

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        Animal.add_dog(Animal, self)

