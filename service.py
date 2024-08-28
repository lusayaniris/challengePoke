import random
from datasource import pokemon_data


class PokemonService:
    def __init__(self):
        self.pokemon_data = pokemon_data

    def get_pokemon_type(self, name):
        """Get the type of a Pokemon by its name."""
        for pokemon in self.pokemon_data:
            if pokemon["name"].lower() == name.lower():
                return pokemon["type"]
        raise ValueError(f"Pokemon with name '{name}' not found.")

    def get_random_pokemon_by_type(self, poke_type):
        """Get a random Pokemon by its type."""
        pokemons_of_type = [
            pokemon for pokemon in self.pokemon_data
            if (isinstance(pokemon["type"], str) and pokemon["type"].lower() == poke_type.lower()) or
               (isinstance(pokemon["type"], list) and poke_type.lower() in [t.lower() for t in pokemon["type"]])
        ]
        if not pokemons_of_type:
            raise ValueError(f"No Pokemon found for type '{poke_type}'.")
        return random.choice(pokemons_of_type)

    def get_pokemon_with_shortest_name(self, poke_type):
        """Get the Pokemon with the shortest name by its type."""
        pokemons_of_type = [
            pokemon for pokemon in self.pokemon_data
            if (isinstance(pokemon["type"], str) and pokemon["type"].lower() == poke_type.lower()) or
            (isinstance(pokemon["type"], list) and poke_type.lower() in [t.lower() for t in pokemon["type"]])
        ]
        if not pokemons_of_type:
            raise ValueError(f"No Pokemon found for type '{poke_type}'.")
        return min(pokemons_of_type, key=lambda p: len(p["name"]))

    def get_pokemon_with_longest_name(self, poke_type):
        """Get the Pokemon with the longest name by its type."""
        pokemons_of_type = [
            pokemon for pokemon in self.pokemon_data
            if (isinstance(pokemon["type"], str) and pokemon["type"].lower() == poke_type.lower()) or
               (isinstance(pokemon["type"], list) and poke_type.lower() in [t.lower() for t in pokemon["type"]])
        ]
        if not pokemons_of_type:
            raise ValueError(f"No Pokemon found for type '{poke_type}'.")
        return max(pokemons_of_type, key=lambda p: len(p["name"]))

    def get_number_of_pokemon(self):
        """Get the number of Pokemon in the datasource."""
        return len(self.pokemon_data)

    def get_pokemon_types(self):
        """Get all unique Pokemon types."""
        types = set()
        for pokemon in self.pokemon_data:
            if isinstance(pokemon["type"], str):
                types.add(pokemon["type"])
            else:
                types.update(pokemon["type"])
        return list(types)

    def get_pokemon_data(self):
        """Get all Pokemon data."""
        return self.pokemon_data

    def get_pokemon_names_by_type(self, poke_type):
        """Get all Pokemon of a type."""
        pokemons_of_type = [
            pokemon for pokemon in self.pokemon_data
            if (isinstance(pokemon["type"], str) and pokemon["type"].lower() == poke_type.lower()) or
               (isinstance(pokemon["type"], list) and poke_type.lower() in [t.lower() for t in pokemon["type"]])
        ]
        if not pokemons_of_type:
            raise ValueError(f"No Pokemon found for type '{poke_type}'.")
        # return the names
        return [pokemon["name"] for pokemon in pokemons_of_type]
