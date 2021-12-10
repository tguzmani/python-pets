from classes.Pet import Pet


class Bird(Pet):
    def __init__(self, admission_date, departure_date, price, food):
        super().__init__(admission_date, departure_date, price, food)
