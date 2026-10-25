import random
import requests

pokemon = ["alcremie", "audino", "clefairy", "cresselia", "diancie", "espeon", "gastrodon", "jiggypuff", "lurantis", "scream-tail", "skitty", "sylveon", ]

def get_pokemon(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(url, timeout=10)

        pokemon_data = response.json()

        return {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"]
        }

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")