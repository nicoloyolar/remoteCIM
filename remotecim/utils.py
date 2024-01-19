import serial
import time

def enviar_comando(puerto_serial, comando):
    puerto_serial.write(comando.encode() + b'\r')
    time.sleep(0.1)
    respuesta = puerto_serial.readline().decode().strip()
    return respuesta