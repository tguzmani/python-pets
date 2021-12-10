from datetime import datetime


class Pet:
    def __init__(self, admission_date, departure_date, price, food):
        self.admission_date = self.__parse_date(admission_date)
        self.departure_date = self.__parse_date(departure_date)
        self.price = float(price)
        self.food = str(food)

    def __parse_date(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%d")

    def __str__(self):
        return "Admission: {}, Departure: {}, Price: ${}, Food: {}".format(
            self.admission_date.strftime("%Y-%m-%d"),
            self.departure_date.strftime("%Y-%m-%d"),
            self.price,
            self.food
        )
