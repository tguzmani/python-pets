from classes.mammals.Mammal import Mammal


class Dog(Mammal):
    def __init__(self, name, admission_date, departure_date, price, food, breed):
        super().__init__(self, admission_date, departure_date, price, food)
        self.name = name
        self.breed = breed

    def __str__(self):
        return "[Dog] " + super().__str__() + ", Breed: {}".format(self.breed)
