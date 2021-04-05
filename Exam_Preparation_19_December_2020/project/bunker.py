from project.supply.supply import Supply

from project.medicine.medicine import Medicine

from project.survivor import Survivor


class Bunker:
    def __init__(self, survivors, supplies, medicine):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"]
        if not food_supplies:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [x for x in self.supplies if x.__class__.__name__ == "WaterSupply"]
        if not water_supplies:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkiller_supplies = [x for x in self.supplies if x.__class__.__name__ == "Painkiller"]
        if not painkiller_supplies:
            raise IndexError("There are no painkillers left!")
        return painkiller_supplies

    @property
    def salves(self):
        salves_supplies = [x for x in self.supplies if x.__class__.__name__ == "Salves"]
        if not salves_supplies:
            raise IndexError("There are no salves left!")
        return salves_supplies

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Salve":
                needed = self.salves.pop()
            else:
                needed = self.painkillers.pop()
            self.medicine.remove(needed)
            needed.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"
        return

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                needed = self.food.pop()
            else:
                needed = self.water.pop()
            self.supplies.remove(needed)
            needed.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"
        return

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age*2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")








