class Pokemon:
    def __init__(self, nombre, tipo, salud=100):
        self.nombre = nombre
        self.tipo = tipo
        self.salud = salud

    def atacar(self, otro_pokemon):
        danio = 10
        print(f"{self.nombre} ataca a {otro_pokemon.nombre} y le causa {danio} de daño!")
        otro_pokemon.recibir_danio(danio)

    def recibir_danio(self, danio):
        self.salud -= danio
        if self.salud <= 0:
            print(f"{self.nombre} se debilitó!")
        else:
            print(f"{self.nombre} tiene {self.salud} de salud restante.")


class Pokedex:
    def __init__(self):
        self.pokemon_lista = []

    def agregar_pokemon(self, pokemon):
        self.pokemon_lista.append(pokemon)

    def eliminar_pokemon(self, nombre):
        for pokemon in self.pokemon_lista:
            if pokemon.nombre == nombre:
                self.pokemon_lista.remove(pokemon)
                print(f"{nombre} ha sido eliminado de la Pokedex.")
                return
        print(f"No se encontró ningún Pokémon con el nombre {nombre}.")

    def mostrar_pokemon(self):
        print("Pokémon en la Pokedex:")
        for pokemon in self.pokemon_lista:
            print(f"Nombre: {pokemon.nombre}, Tipo: {pokemon.tipo}, Salud: {pokemon.salud}")

    def batalla(self, nombre1, nombre2):
        pokemon1 = None
        pokemon2 = None

        for pokemon in self.pokemon_lista:
            if pokemon.nombre == nombre1:
                pokemon1 = pokemon
            if pokemon.nombre == nombre2:
                pokemon2 = pokemon

        if not pokemon1 or not pokemon2:
            print("No se pueden realizar batallas. Asegúrate de que ambos Pokémon estén en la Pokedex.")
            return

        print(f"¡Batalla entre {pokemon1.nombre} y {pokemon2.nombre}!")
        while pokemon1.salud > 0 and pokemon2.salud > 0:
            pokemon1.atacar(pokemon2)
            if pokemon2.salud <= 0:
                print(f"{pokemon1.nombre} ganó la batalla!")
                break
            pokemon2.atacar(pokemon1)
            if pokemon1.salud <= 0:
                print(f"{pokemon2.nombre} ganó la batalla!")


# Crear una Pokedex
pokedex = Pokedex()

# Agregar Pokémon
pikachu = Pokemon("Pikachu", "Eléctrico", 100)
charmander = Pokemon("Charmander", "Fuego", 100)
bulbasaur = Pokemon("Bulbasaur", "Planta", 100)

pokedex.agregar_pokemon(pikachu)
pokedex.agregar_pokemon(charmander)
pokedex.agregar_pokemon(bulbasaur)

# Mostrar Pokémon en la Pokedex
pokedex.mostrar_pokemon()

# Realizar una batalla
pokedex.batalla("Pikachu", "Charmander")

# Eliminar un Pokémon
pokedex.eliminar_pokemon("Bulbasaur")

# Mostrar Pokémon actualizados en la Pokedex
pokedex.mostrar_pokemon()
