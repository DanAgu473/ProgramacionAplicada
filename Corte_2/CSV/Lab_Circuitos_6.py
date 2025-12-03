import serial
import time
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets, QtCore
from collections import deque

puerto = "COM5"
baudrate = 115200

ser = serial.Serial(puerto, baudrate, timeout=0.1)
ser.reset_input_buffer()

# Buffers
max_puntos = 500
tiempos = deque(maxlen=max_puntos)
valores = deque(maxlen=max_puntos)

#PyQtGraph suavizar
pg.setConfigOptions(antialias=True)

# PyQtGraph
app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(show=True, title="Lectura Tiempo Real - ESP32")
plot = win.addPlot(title="Curva de carga/descarga (V1 - V2)")
curve = plot.plot(pen=pg.mkPen("y", width=2, antialias=True))

plot.setLabel('left', "Voltaje (V)")
plot.setLabel('bottom', "Muestras")
plot.showGrid(x=True, y=True)

contador = 0

def actualizar():
    global contador

    if ser.in_waiting:
        raw = ser.readline().decode('utf-8', errors='ignore').strip()

        if "V1:" not in raw or "V2:" not in raw:
            return

        try:
            partes = raw.replace("V1:", "").replace("V2:", "").split(",")
            v1 = float(partes[0])
            v2 = float(partes[1])
        except:
            return

        diff = v1 - v2

        tiempos.append(contador)
        valores.append(diff)
        contador += 1

        curve.setData(list(tiempos), list(valores))

        if ser.in_waiting > 200:
            ser.reset_input_buffer()

timer = QtCore.QTimer()
timer.timeout.connect(actualizar)
timer.start(5)

QtWidgets.QApplication.instance().exec_()
