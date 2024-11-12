import requests
import json
from datetime import datetime

class PokemonApi:
    def __init__(self, endpoint_file="scraper/pokemon_list.json", checkpoint_file="extracted_pokemon.json"):
        self.base_url = "https://pokeapi.co/api/v2/"
        self.endpoint_file = endpoint_file
        self.checkpoint_file = checkpoint_file

    def _load_checkpoint(self):
        try:
            with open(self.checkpoint_file, "r") as file:
                extracted = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            extracted = []
        return extracted

    def _save_checkpoint(self, extracted):
        with open(self.checkpoint_file, "w") as file:
            json.dump(extracted, file, indent=4)

    def _load_pokemon_list(self):
        try:
            with open(self.endpoint_file, "r") as file:
                pokemon_endpoints = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pokemon_endpoints = []
        return pokemon_endpoints

    def _save_pokemon_data(self, pokemon_name):
        timestamp = datetime.now().isoformat()
        pokemon_data = {
            "name": pokemon_name,
            "timestamp": timestamp
        }

        with open(f"{pokemon_name}_{timestamp}.json", "w") as file:
            json.dump(pokemon_data, file, indent=4)

    def get_data(self):
        extracted = self._load_checkpoint()

        pokemon_endpoints = self._load_pokemon_list()

        for endpoint in pokemon_endpoints:
            if endpoint in extracted:
                print(f"{endpoint} has already been extracted.")
                continue

            url = f"{self.base_url}{endpoint}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                pokemon_name = data.get("name", "unknown")
                
                # Save Pokémon data in a separate method
                self._save_pokemon_data(pokemon_name)

                print(f"Data for {pokemon_name} saved successfully.")

                extracted.append(endpoint)
                self._save_checkpoint(extracted)
            else:
                print(f"Error: {response.status_code} for {endpoint}")


a = PokemonApi()
a.get_data()
