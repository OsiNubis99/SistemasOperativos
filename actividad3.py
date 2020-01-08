import socket,sys

connection = socket.socket()
archivo = open("numeros.txt","r")
connection.connect(('localhost',9999))
data = archivo.readlines()
fuente = 0
for line in data:
	connection.send(input(line))
	fuente += connection.recv(1024)
print(fuente)
archivo.close
connection.close()