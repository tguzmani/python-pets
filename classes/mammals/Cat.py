from classes.mammals.Mammal import Mammal


class Cat(Mammal):
    def __init__(self, name, admission_date, departure_date, price, food, breed):
        super().__init__(self, admission_date, departure_date, price, food)
        self.name = name
        self.breed = breed

    def __str__(self):
        return "[Cat] " + super().__str__() + ", Breed: {}".format(self.breed)
