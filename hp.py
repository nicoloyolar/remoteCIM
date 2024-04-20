import socket
import time
import serial
import threading
import re

def enviar_comando(puerto_serial, comando):
    """Esta función permite enviar un comando mediante el puerto serial"""
    puerto_serial.write(comando.encode() + b'\r')
    time.sleep(0.1)

def manejar_respuesta(respuesta):
    """Esta función permite gestionar la respuesta cuando se almacena un punto en el robot"""
    prefix_list = ["1:", "2:", "3:", "4:", "5:"]
    values_list = [re.search(prefix + r'\s*(\S+)', respuesta).group(1) for prefix in prefix_list if re.search(prefix + r'\s*(\S+)', respuesta)]
    return ", ".join(values_list)

def manejar_mensaje(client_socket, puerto_serial):
    """Esta función gestiona el mensaje y lo envía mediante protocolo serial hacia el robot"""
    message = client_socket.recv(1024).decode()
    enviar_comando(puerto_serial, message)
    
    time.sleep(1)
    
    respuesta = puerto_serial.read_all().decode().strip()
    
    print("Respuesta:", respuesta)
    
    values_string = manejar_respuesta(respuesta)
    print("Valores encontrados:", values_string) 
    
    # Envía la respuesta de vuelta por el mismo socket
    client_socket.send(values_string.encode())
    client_socket.close()

def escuchar_socket(puerto_serial):
    """Esta función es quien permite recibir datos mediante socket"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(10)

    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=manejar_mensaje, args=(client_socket, puerto_serial))
        thread.start()

try:
    with serial.Serial('COM4', baudrate=9600, timeout=1) as puerto_serial:
        thread_socket = threading.Thread(target=escuchar_socket, args=(puerto_serial,))
        thread_socket.start()

        while True:
            mensaje = input("Ingrese el comando a enviar al robot: ")
            
            enviar_comando(puerto_serial, mensaje)
            
            time.sleep(1)
            
            respuesta = puerto_serial.read_all().decode().strip()
            print("Respuesta:", respuesta)
            
            values_string = manejar_respuesta(respuesta)
            print("Valores encontrados:", values_string)

except serial.SerialException as e:
    print("Error:", str(e))
    
except KeyboardInterrupt:
    print("Interrupción del usuario")
    
except Exception as e:
    print("Error:", str(e))
