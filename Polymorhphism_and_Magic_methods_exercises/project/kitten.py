from project.animal import Animal
from project.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.GENDER)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.GENDER} {self.__class__.__name__}"

    def make_sound(self):
        return f"Meow"



