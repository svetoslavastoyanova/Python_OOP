from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.base_decoration import BaseDecoration
from project.decoration.decoration_repository import DecorationRepository
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = [] # ALL aquarium objects

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if not aquarium_type == "FreshwaterAquarium" or not aquarium_type == "SaltwaterAquarium":
            return f"Invalid aquarium type."
        else:
            if aquarium_type == "FreshwaterAquarium":
                aquarium = FreshwaterAquarium(aquarium_name)
                self.aquariums.append(aquarium)
            elif aquarium_type == "SaltwaterAquarium":
                aquarium = SaltwaterAquarium(aquarium_name)
                self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if not decoration_type == "Ornament" or not decoration_type == "Plant":
            return f"Invalid decoration type."
        else:
            if decoration_type == "Ornament":
                decoration = DecorationRepository()
                self.decorations_repository.add(decoration)
            elif decoration_type == "Plant":
                decoration = DecorationRepository()
                self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [a for a in self.aquariums if aquarium_name == a.name][0]
        decoration_type_exists = self.decorations_repository.find_by_type(decoration_type)
        if aquarium and (decoration_type_exists != 'None'):
            self.decorations_repository.remove(decoration_type_exists)
            aquarium.add_decoration(decoration_type_exists)
            return f'Successfully added {decoration_type} to {aquarium_name}.'
        if not decoration_type_exists:
            return f"There isn't a decoration of type {decoration_type}."


    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        aquarium = [x for x in self.aquariums if aquarium_name == x.name][0]
        if fish_type == 'FreshwaterFish':
            fish_to_add = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == 'SaltwaterFish':
            fish_to_add = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."
        return aquarium.add_fish(fish_to_add)

    def feed_fish(self, aquarium_name: str):
        fed_fishes = [x.feed() for x in self.aquariums if x.name == aquarium_name]
        return f"Fish fed: {fed_fishes}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [x for x in self.aquariums if x == aquarium_name][0]
        fish_prices = sum([x.price for x in self.aquariums if isinstance(x, BaseFish)])
        decoration_prices = sum([x.price for x in self.aquariums if isinstance(x, BaseDecoration)])
        result = fish_prices + decoration_prices
        return f"The value of Aquarium {aquarium_name} is {result:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += aquarium.__str__()
        return result



