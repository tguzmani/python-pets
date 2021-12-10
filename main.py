from classes.mammals.Cat import Cat
from classes.mammals.Dog import Dog

from classes.reptiles.Iguana import Iguana
from classes.reptiles.Snake import Snake

from classes.birds.Canary import Canary
from classes.birds.Parakeet import Parakeet


if __name__ == "__main__":
    pets = [
        Cat("Mimo", "2021-12-01", "2021-12-10", 600, "Meow Mix", "Siamese"),

        Dog("Lucky", "2021-12-01", "2021-12-10",
            1000, "Pedigree", "Golden Retriever"),

        Iguana("Balerion", "2021-12-01", "2021-12-10", 250, "Zoo Med"),

        Snake("Asmodeus", "2021-12-01", "2021-12-10", 200, "Rodents"),

        Canary("2021-12-01", "2021-12-10", 80, "Prestige"),

        Parakeet("2021-12-01", "2021-12-10", 100, "Kaytee"),
    ]

    for pet in pets:
        print(pet)
