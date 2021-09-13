from Animal.animals.animal import Bird
from Animal.food import Meat, Vegetable, Fruit, Food


class Owl(Bird):
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25*food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return f"Hoot Hoot"


class Hen(Bird):
    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return f"Cluck"

