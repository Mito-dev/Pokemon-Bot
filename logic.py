import aiohttp  # A library for asynchronous HTTP requests
import random

class Pokemon:
    pokemons = {}
    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.img = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # Metode asinkron untuk mendapatkan nama pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API untuk permintaan
        async with aiohttp.ClientSession() as session:  # Membuka HTTP session
            async with session.get(url) as response:  # Mengirim permintaan GET
                if response.status == 200:
                    data = await response.json()  # Menerima dan mendekode respons JSON
                    return data['forms'][0]['name']  # Mengembalikan nama Pokémon
                else:
                    return "Pikachu"  # Kembalikan nama default jika permintaan gagal
                # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['sprites'][0]['other']['showdown']['front_default']  # Returning a Pokémon's name
                else:
                    return None  # Return the default name if the request fails