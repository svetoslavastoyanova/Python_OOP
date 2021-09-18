class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        try:
            filtered_pokemon = [p for p in self.pokemon if p.name == pokemon_name][0]
            self.pokemon.remove(filtered_pokemon)
            return f"You have released {pokemon_name}"
        except IndexError:
            return "Pokemon is not caught"

    def trainer_data(self):
        trainer_info = f"Pokemon Trainer {self.name}\n" \
                 f"Pokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            trainer_info += f"- {p.pokemon_details()}\n"
        return trainer_info


