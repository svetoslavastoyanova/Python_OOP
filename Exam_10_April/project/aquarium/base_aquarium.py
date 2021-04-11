from abc import ABC, abstractmethod


class BaseAquarium:
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []  # decorations objects
        self.fish = [] # all fish objects
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return f"Not enough capacity."
        else:
            if fish.__class__.__name__ == "FreshwaterFish" or fish.__class__.__name__ == "SaltwaterFish":
                self.fish.append(fish)
                self.capacity += 1
                return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        result = [x.eat() for x in self.fish]

    def __str__(self):
        result = ""
        result += f"{self.name}:"
        for fish in self.fish:
            result += f"Fish: {fish.name}\n"
            if not fish:
                result += "none"
        for dec in self.decorations:
            result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result


