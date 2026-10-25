import random
import requests

pokemon = ["alcremie", "espeon", "lurantis", "skitty", "sylveon", ]

def get_pokemon(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print("\nError: Pokemon was not found.")

        response.raise_for_status()

        pokemon_data = response.json()

        return {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"]
        }

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")

def guessing_game():

    target_pokemon = random.choice(pokemon)

    pokemon_data = get_pokemon(target_pokemon)

    name = pokemon_data["name"]
    height = pokemon_data["height"]
    weight = pokemon_data["weight"]

    print("==== WHO'S THAT POKEMON? =====")
    print("Guess the Pokemon based on it's height and weight!")
    print("You have 3 chances to guess.")
    print("Good Luck!\n")

    print(30 * "=")

    print("\nWho's pokemon is...")
    print(f"Height: {height}")
    print(f"Weight: {weight}")

    for attempt in range(3):

        guess = input("\nGuess the Pokemon: ").lower().strip()

        if guess == name:
            print("You are right!")
            break
        else:
            print("Wrong guess! Try again.")

guessing_game()