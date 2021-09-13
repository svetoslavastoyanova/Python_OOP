from Animal.animals.animal import Mammal
from Animal.food import Meat, Vegetable, Seed, Fruit


class Mouse(Mammal):
    def feed(self, food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return f"Squeak"


class Dog(Mammal):
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return f"Woof!"


class Cat(Mammal):
    def feed(self, food):
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return f"Meow"


class Tiger(Mammal):
    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1.0 * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return f"ROAR!!!"