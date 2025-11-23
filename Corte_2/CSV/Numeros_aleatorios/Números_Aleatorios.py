import csv
import random

archivo = 'numeros.csv'

numeros_aleatorios = [random.randint(1, 100) for _ in range(100)]

with open(archivo, mode='w', newline='') as file:  # 'w' sobreescribe el archivo
    writer = csv.writer(file)
    writer.writerow(['Numero'])  # Encabezado opcional
    for numero in numeros_aleatorios:
        writer.writerow([numero])

print(f"Se generaron y guardaron 100 números aleatorios en el archivo: {archivo}")
