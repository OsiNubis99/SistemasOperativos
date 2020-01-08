import subprocess,sys

archivo = open("numeros.txt","r")
data = archivo.readlines()
fuente = 0
for line in data:
	fuente += int(subprocess.check_output(['python3', 'fuente1.py', sys.argv[1], line]))
print(fuente)
archivo.close