# #### Get A Key
# Inicializa el diccionario 'building_heights' con nombres de edificios (claves) y sus alturas (valores).
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# Accede al valor asociado a la clave "Burj Khalifa" (828).
print(building_heights["Burj Khalifa"])
# Accede al valor asociado a la clave "Ping An" (599).
print(building_heights["Ping An"])

# Inicializa el diccionario 'zodiac_elements'. Las claves son elementos, los valores son listas de signos.
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# Accede e imprime la lista de signos asociados a la clave "earth".
print(zodiac_elements["earth"])
# Accede e imprime la lista de signos asociados a la clave "fire".
print(zodiac_elements["fire"])

# ## Get an Invalid Key
# Inicializa el diccionario 'building_heights'.
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# Esta línea **PRODUCE UN ERROR (KeyError)** porque la clave "Landmark 81" no existe.
# La he mantenido aquí pero no se ejecutará en un entorno real después de este punto.
# print(building_heights["Landmark 81"])

# ## One way to avoid this error is to first check if the key exists in the dictionary:
# Define la clave a buscar.
key_to_check = "Landmark 81"

# Comprueba si la clave existe en el diccionario 'building_heights'.
if key_to_check in building_heights:
   # Si existiera, imprime su valor. Como no existe, el bloque se salta.
   print(building_heights["Landmark 81"])

# Inicializa el diccionario 'zodiac_elements'.
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# Agrega la nueva clave "energy" al diccionario.
zodiac_elements["energy"] = "Not a Zodiac element"

# Comprueba si "energy" existe en el diccionario.
if "energy" in zodiac_elements:
   # Imprime el valor asociado, ya que la clave fue agregada en la línea anterior.
   print(zodiac_elements["energy"])

# ##Safely Get a Key
# Inicializa el diccionario 'building_heights'.
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Usa el método .get() para obtener el valor; retorna 632.
building_heights.get("Shanghai Tower")

# Usa .get() con una clave inexistente; retorna None (y evita el KeyError).
building_heights.get("My House")

# ###
# Inicializa el diccionario 'user_ids'.
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# Obtiene el valor de "teraCoder" (100019).
user_ids.get("teraCoder")

# Comprueba si el valor retornado por .get() es None (es decir, si la clave no existía).
if user_ids.get("teraCoder") == None:
   # Si la clave NO existiera, asignaría 1000.
   tc_id = 1000
else:
   # Como la clave EXISTE, asigna el valor real (100019).
   tc_id = user_ids.get("teraCoder")

# Imprime el valor final de tc_id (100019).
print(tc_id)

# Comprueba si "superStackSmash" existe. Como no existe, .get() retorna None.
if user_ids.get("superStackSmash") == None:
      # Como es None, el bloque se ejecuta y asigna 100000.
      stack_id = 100000

# Imprime el valor final de stack_id (100000).
print(stack_id)

# ###Delete a Key
# Inicializa el diccionario 'raffle'.
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
# Usa .pop() para eliminar la clave 320291. Retorna "Gift Basket".
print(raffle.pop(320291, "No Prize"))
# Imprime el diccionario modificado (sin 320291).
print(raffle)
# Intenta eliminar la clave 100000. Como no existe, retorna el valor por defecto ("No Prize").
print(raffle.pop(100000, "No Prize"))
# Imprime el diccionario sin cambios.
print(raffle)
# Elimina la clave 872921. Retorna "Concert Tickets".
print(raffle.pop(872921, "No Prize"))
# Imprime el diccionario final.
print(raffle)

# Inicializa el diccionario de ítems y la variable de puntos de vida.
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# Elimina "stamina grains". Su valor (15) se retorna y se suma a health_points.
health_points += available_items.pop("stamina grains", 0)
# Elimina "power stew". Su valor (30) se retorna y se suma a health_points.
health_points += available_items.pop("power stew", 0)
# Intenta eliminar "mystic bread". Como no existe, retorna el valor por defecto (0) y lo suma.
health_points += available_items.pop("mystic bread", 0)

# Imprime el diccionario con los ítems restantes.
print(available_items)
# Imprime el total de puntos de vida (20 + 15 + 30 + 0 = 65).
print(health_points)

# ##Get All Keys
# Inicializa el diccionario 'test_scores'.
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
# Convierte el objeto iterable de claves en una lista y la imprime.
print(list(test_scores))

# Itera a través de las claves del diccionario usando el método .keys() (explícito).
for student in test_scores.keys():
 print(student)

# Inicializa los diccionarios 'user_ids' y 'num_exercises'.
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Obtiene los objetos de vista de las claves de ambos diccionarios.
users = user_ids.keys()
lessons = num_exercises.keys()

# Imprime los objetos de vista de claves (dict_keys([...])).
print(users)
print(lessons)

# ##Get All Values
# Inicializa el diccionario 'test_scores'.
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# Itera sobre los valores del diccionario usando el método .values().
for score_list in test_scores.values():
 print(score_list)

# Inicializa el diccionario 'num_exercises'.
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Inicializa el contador.
total_exercises = 0

# Itera sobre los valores (números de ejercicios) del diccionario.
for exercises in num_exercises.values():
   # Suma cada valor al contador.
   total_exercises += exercises
# Imprime la suma total de ejercicios.
print(total_exercises)

# ##Get All Items
# Inicializa el diccionario 'biggest_brands'.
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# Itera sobre los pares clave-valor (items) del diccionario usando .items().
# Las variables 'company' y 'value' toman los valores del par en cada iteración.
for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")

# Inicializa el diccionario 'pct_women_in_occupation'.
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# Itera sobre los pares clave-valor del diccionario.
for occupation, percentage in pct_women_in_occupation.items():
   # Imprime un mensaje formateado con los datos de cada par.
   print("Women make up " + str(percentage) + " percent of " + occupation + "s.")