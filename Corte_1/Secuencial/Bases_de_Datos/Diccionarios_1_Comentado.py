# Crea el diccionario 'sensors' para almacenar temperaturas (valores) asociadas a ubicaciones (claves).
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# Crea el diccionario 'num_cameras' para almacenar el número de cámaras (valores) por ubicación (claves).
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Imprime el diccionario 'sensors'.
print(sensors)
# Imprime el diccionario 'num_cameras'.
print(num_cameras)

# Crea un diccionario para traducciones, donde la clave es la palabra en inglés y el valor es la traducción.
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
# Imprime el diccionario 'translations'.
print(translations)

## Verifiying an error:
# La línea 'powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}' genera un error
# porque las listas [] son objetos mutables y NO pueden usarse como claves de diccionario.
# Solo los tipos de datos inmutables (tuplas, strings, números) pueden ser claves.

# Crea el diccionario 'children' con nombres de familia (claves) y una lista de nombres (valores).
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
# Imprime el diccionario 'children'.
print(children)

# Crea y asigna un diccionario vacío a 'my_empty_dictionary'.
my_empty_dictionary = {}
# Imprime el diccionario vacío {}.
print(my_empty_dictionary)

# Inicializa el diccionario 'menu' con elementos y sus precios.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Imprime el estado inicial del diccionario.
print("Before: ", menu)
# Agrega una nueva clave-valor ("cheesecake": 8) al diccionario 'menu'.
menu["cheesecake"] = 8
# Imprime el diccionario después de la adición.
print("After", menu)

# Inicializa el diccionario 'animals_in_zoo'.
animals_in_zoo = {"dinosaurs": 0}
# Sobreescribe la clave "dinosaurs" con el valor 0 (repite la línea anterior).
animals_in_zoo = {"dinosaurs": 0}
# Sobreescribe el diccionario completo con uno nuevo: {"horses": 2}.
animals_in_zoo = {"horses": 2}
# Imprime el diccionario final.
print(animals_in_zoo)


## Add multiple keys
# Inicializa el diccionario 'sensors'.
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

# Usa el método update() para agregar múltiples pares clave-valor al diccionario 'sensors'.
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

###
# Inicializa el diccionario 'user_ids'.
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
# Agrega múltiples usuarios y sus IDs usando update().
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

## Overwrite Values ##
# Inicializa el diccionario 'menu'.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
# Sobreescribe el valor asociado a la clave "oatmeal" (cambia de 3 a 5).
menu["oatmeal"] = 5
print("After", menu)

# Inicializa el diccionario 'oscar_winners'.
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
# Agrega el par clave-valor "Supporting Actress": "Viola Davis" usando update().
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()
# Sobreescribe el valor de la clave "Best Picture" (cambia de "La La Land" a "Moonlight").
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)


###Dict Comprehensions
# Define una lista de nombres.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# Define una lista de alturas.
heights = [61, 70, 67, 64]

# La función zip() combina las dos listas en un iterador de tuplas (par nombre, altura).
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents) # Imprime el objeto iterador zip.

# Crea el diccionario 'students' usando una *dict comprehension* que itera sobre los pares generados por zip().
# Cada par (key, value) se convierte en un elemento del diccionario.
students = {key:value for key, value in zip(names, heights)}
print(students)

# Define una lista de bebidas.
drinks = ["espresso", "chai", "decaf", "drip"]
# Define una lista de niveles de cafeína.
caffeine = [64, 40, 0, 120]

# Combina las dos listas en un iterador de tuplas.
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

# Crea el diccionario 'drinks_to_caffeine' usando una *dict comprehension* a partir de los pares de zip.
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

# Define una lista de canciones.
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# Define una lista de conteos de reproducción.
playcounts = [78, 29, 44, 21, 89, 5]
# Crea el diccionario 'plays' combinando las dos listas usando zip y una *dict comprehension*.
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

# Agrega la canción "Purple Haze" con un conteo de 1 usando update().
plays.update({"Purple Haze": 1})
# Sobreescribe el conteo de "Respect" de 89 a 94 usando update().
plays.update({"Respect": 94})
print("After: ", plays)

# Crea un diccionario anidado 'library', donde una clave apunta a otro diccionario.
# "The Best Songs" apunta al diccionario 'plays'. "Sunday Feelings" apunta a un diccionario vacío.
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)