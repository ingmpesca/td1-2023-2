class Pokemon:
    def __init__(self, nombre, tipo, salud=100, ataque=10, defensa=5, experiencia=0):
        self.nombre = nombre
        self.tipo = tipo
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.experiencia = experiencia

    def atacar(self, otro_pokemon):
        danio = self.ataque - otro_pokemon.defensa
        danio = max(danio, 0)
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
        print(f"{pokemon.nombre} ha sido agregado a la Pokedex.")

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
            print(f"Nombre: {pokemon.nombre}, Tipo: {pokemon.tipo}, Salud: {pokemon.salud}, Ataque: {pokemon.ataque}, Defensa: {pokemon.defensa}, Experiencia: {pokemon.experiencia}")

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
                pokemon1.experiencia += 10
                print(f"{pokemon1.nombre} ganó 10 puntos de experiencia.")
                break
            pokemon2.atacar(pokemon1)
            if pokemon1.salud <= 0:
                print(f"{pokemon2.nombre} ganó la batalla!")
                pokemon2.experiencia += 10
                print(f"{pokemon2.nombre} ganó 10 puntos de experiencia.")


# Crear una Pokedex
pokedex = Pokedex()

while True:
    print("\nOpciones:")
    print("1. Agregar Pokémon")
    print("2. Mostrar Pokémon")
    print("3. Realizar Batalla")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del Pokémon: ")
        tipo = input("Tipo del Pokémon: ")
        salud = int(input("Salud del Pokémon: "))
        ataque = int(input("Ataque del Pokémon: "))
        defensa = int(input("Defensa del Pokémon: "))
        experiencia = int(input("Experiencia del Pokémon: "))
        nuevo_pokemon = Pokemon(nombre, tipo, salud, ataque, defensa, experiencia)
        pokedex.agregar_pokemon(nuevo_pokemon)

    elif opcion == "2":
        pokedex.mostrar_pokemon()

    elif opcion == "3":
        nombre1 = input("Nombre del primer Pokémon en la batalla: ")
        nombre2 = input("Nombre del segundo Pokémon en la batalla: ")
        pokedex.batalla(nombre1, nombre2)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")



# Crear una Pokedex
pokedex = Pokedex()

while True:
    print("\nOpciones:")
    print("1. Agregar Pokémon")
    print("2. Mostrar Pokémon")
    print("3. Realizar Batalla")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del Pokémon: ")
        tipo = input("Tipo del Pokémon: ")
        salud = int(input("Salud del Pokémon: "))
        ataque = int(input("Ataque del Pokémon: "))
        defensa = int(input("Defensa del Pokémon: "))
        experiencia = int(input("Experiencia del Pokémon: "))
        nuevo_pokemon = Pokemon(nombre, tipo, salud, ataque, defensa, experiencia)
        pokedex.agregar_pokemon(nuevo_pokemon)
        print(f"{nombre} ha sido agregado a la Pokedex.")

    elif opcion == "2":
        pokedex.mostrar_pokemon()

    elif opcion == "3":
        nombre1 = input("Nombre del primer Pokémon en la batalla: ")
        nombre2 = input("Nombre del segundo Pokémon en la batalla: ")
        pokedex.batalla(nombre1, nombre2)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

