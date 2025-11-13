import serial
import time
import re

# 📌 Configuración del puerto y archivo
puerto = 'COM5'       # Cambia esto según tu ESP32
baudrate = 115200
archivo = 'lecturas.csv'

# 🕓 Conexión con el ESP32
ser = serial.Serial(puerto, baudrate, timeout=1)
time.sleep(3)  # Espera que termine el bootloader del ESP32

# 🧹 Limpia el buffer del arranque
ser.reset_input_buffer()

# ✍️ Encabezados del CSV
encabezado = "Tiempo(s),Lectura_ADC,Voltaje(V)"

# 🧩 Patrón para aceptar solo líneas tipo CSV
patron_csv = re.compile(r'^-?\d+(\.\d+)?,\s*\d+,\s*\d+(\.\d+)?$', re.IGNORECASE)

# 📂 ABRIR EL ARCHIVO EN MODO *WRITE* PARA REESCRIBIR DESDE CERO
with open(archivo, 'w', encoding='utf-8') as f:
    # Escribir encabezado siempre
    f.write(encabezado + '\n')

    print("📡 Grabando datos del ESP32 en", archivo)
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
        print("\n✅ Lectura detenida por el usuario.")
    finally:
        ser.close()
        print(f"📁 Datos guardados correctamente en '{archivo}'.")