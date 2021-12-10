from classes.reptiles.Reptile import Reptile


class Iguana(Reptile):
    def __init__(self, name, admission_date, departure_date, price, food):
        super().__init__(self, admission_date, departure_date, price, food)
        self.name = name

    def __str__(self):
        return "[Iguana] Name: {}, ".format(self.name) + super().__str__()
