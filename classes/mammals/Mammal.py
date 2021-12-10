from classes.Pet import Pet


class Mammal(Pet):
    def __init__(self, name, admission_date, departure_date, price, food):
        self.name = name
        super().__init__(admission_date, departure_date, price, food)

    def __str__(self):
        return "Name: {}, ".format(self.name) + super().__str__()
