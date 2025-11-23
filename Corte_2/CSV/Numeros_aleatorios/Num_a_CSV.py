import serial
import time
import re
import matplotlib.pyplot as plt

puerto = 'COM5'
baudrate = 115200
archivo = 'numeros.csv'

# Conexión con el ESP32 via puerto serial
ser = serial.Serial(puerto, baudrate, timeout=1)
time.sleep(3)
ser.reset_input_buffer()

encabezado = "Tiempo(s),Numero_Aleatorio"
patron_csv = re.compile(r'^-?\d+(\.\d+)?,\s*\d+,\s*\d+(\.\d+)?$', re.IGNORECASE)

tiempos = []
numeros = []

plt.ion()
fig, ax = plt.subplots()

with open(archivo, 'w', encoding='utf-8') as f:

    f.write(encabezado + '\n')

    print("Presiona Ctrl+C para detener...")

    try:
        while True:

            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            if not linea:
                continue


            if patron_csv.match(linea):
                
                f.write(linea + '\n')
                f.flush()
                print(linea)

                partes = linea.split(',')
                t = float(partes[0])
                n = float(partes[1])

                tiempos.append(t)
                numeros.append(n)

                ax.clear()
                ax.plot(tiempos, numeros)
                ax.set_xlabel("Tiempo (s)")
                ax.set_ylabel("Número")
                ax.set_title("Lectura en tiempo real")
                ax.grid(True)
                plt.pause(0.01)

    except KeyboardInterrupt:
        print("\n Lectura completada; creado el archivo lecturas.csv.")
    finally:
        ser.close()