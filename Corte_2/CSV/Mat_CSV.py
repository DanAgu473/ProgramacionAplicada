import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('lecturas.csv')
x = df.iloc[:, 0]  
y = df.iloc[:, 2]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Tiempo vs Voltaje")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.show()


# Calcular estadísticas básicas
mean_voltage = np.mean(y)
max_voltage = np.max(y)
min_voltage = np.min(y)
std_voltage = np.std(y)
print(f"Voltaje Promedio: {mean_voltage:.2f} V")
print(f"Voltaje Máximo: {max_voltage:.2f} V")
print(f"Voltaje Mínimo: {min_voltage:.2f} V")
print(f"Desviación Estándar del Voltaje: {std_voltage:.2f} V")


x = df.iloc[:, 0]  
y = df.iloc[:, 1]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Tiempo vs Serial_ADC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.show()
