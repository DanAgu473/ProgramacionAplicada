import serial
import time
import re

puerto = 'COM5'      
baudrate = 115200
archivo = 'numeros.csv'

# Conexión con el ESP32 via puerto serial
ser = serial.Serial(puerto, baudrate, timeout=1)
time.sleep(3)  # Espera que termine el bootloader del ESP32

ser.reset_input_buffer()
# encabezado del CSV
encabezado = "Tiempo(s),Numero_Aleatorio"
# Expresión regular para validar líneas CSV
patron_csv = re.compile(r'^-?\d+(\.\d+)?,\s*\d+,\s*\d+(\.\d+)?$', re.IGNORECASE)

with open(archivo, 'w', encoding='utf-8') as f:
    # Escribir encabezado siempre
    f.write(encabezado + '\n')

    print("Presiona Ctrl+C para detener...")

    try:
        while True:
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            if not linea:
                continue

            # Solo aceptar datos válidos
            if patron_csv.match(linea):
                print(linea)
                f.write(linea + '\n')
    except KeyboardInterrupt:
        print("\n Lectura completada; creado el archivo lecturas.csv.")
    finally:
        ser.close()