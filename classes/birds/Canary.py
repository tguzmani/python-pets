from classes.birds.Bird import Bird


class Canary(Bird):
    def __init__(self, admission_date, departure_date, price, food):
        super().__init__(admission_date, departure_date, price, food)

    def __str__(self):
        return "[Canary] " + super().__str__()
