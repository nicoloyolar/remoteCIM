import socket
import time
import serial
import threading
import json

def enviar_comando(puerto_serial, comando):
    puerto_serial.write(comando.encode() + b'\r')
    time.sleep(0.1)

def manejar_mensaje(client_socket, puerto_serial):
    message = client_socket.recv(1024).decode()
    enviar_comando(puerto_serial, message)
    time.sleep(1)
    respuesta = b""
    while puerto_serial.in_waiting > 0:
        respuesta += puerto_serial.read(puerto_serial.in_waiting)
    respuesta = respuesta.decode().strip()
    print(respuesta)
    prefix_list = ["1:", "2:", "3:", "4:", "5:"]
    values_list = []
    for prefix in prefix_list:
        index = respuesta.find(prefix)
        if index != -1:
            value = respuesta[index + len(prefix):].split()[0]
            values_list.append(value)

    # Formatear los valores como una cadena separada por comas
    values_string = ", ".join(values_list)
    
    print(values_string) 
    client_socket.send(values_string.encode())
    client_socket.close()

def escuchar_socket(puerto_serial):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(10)

    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=manejar_mensaje, args=(client_socket, puerto_serial))
        thread.start()

try:
    puerto_serial = serial.Serial('COM5', baudrate=9600, timeout=1)
    
    thread_socket = threading.Thread(target=escuchar_socket, args=(puerto_serial,))
    thread_socket.start()

    while True:
        mensaje = input("Ingrese el comando a enviar al robot: ")
        enviar_comando(puerto_serial, mensaje)
        
        # Esperar un segundo y luego leer y mostrar todas las líneas disponibles
        time.sleep(1)
        respuesta = b""
        while puerto_serial.in_waiting > 0:
            respuesta += puerto_serial.read(puerto_serial.in_waiting)
        respuesta = respuesta.decode().strip()
        print("respuesta: ", respuesta)
        # Buscar y almacenar los valores después de "1:", "2:", "3:", "4:" y "5:" en una lista
        prefix_list = ["1:", "2:", "3:", "4:", "5:"]
        values_list = []
        for prefix in prefix_list:
            index = respuesta.find(prefix)
            if index != -1:
                value = respuesta[index + len(prefix):].split()[0]
                values_list.append(value)

        # Formatear los valores como una cadena separada por comas
        values_string = ", ".join(values_list)
        print("Valores encontrados:", values_string)  # Imprimir valores aquí

except serial.SerialException as e:
    print("Error 1:", str(e))
except serial.SerialTimeoutException:
    print("Error tiempo agotado")
except KeyboardInterrupt:
    print("Interrupción del usuario")

finally:
    puerto_serial.close()
