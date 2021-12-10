from classes.Pet import Pet


class Reptile(Pet):
    def __init__(self, name, admission_date, departure_date, price, food):
        super().__init__(admission_date, departure_date, price, food)
        self.name = name

    def __str__(self):
        return "Name: {}, ".format(self.name) + super().__str__()
