import subprocess,sys
from time import time

tiempo = time()
actividad1 = subprocess.check_output(['python3', 'actividad1.py', sys.argv[1]])
tiempo = time() - tiempo
print("Actividad 1: "+str(int(actividad1)))
print("Tiempo de la actividad 1: "+str(tiempo))

tiempo2 = time()
actividad2 = subprocess.check_output(['python3', 'actividad2.py', sys.argv[2]])
tiempo2 = time() - tiempo2
print("Actividad 2: "+str(float(actividad2)))
print("Tiempo de la actividad 2: "+str(tiempo2))

tiempo3 = 0#time()
# actividad3 = subprocess.check_output(['python3', 'actividad3.py', sys.argv[1], sys.argv[2]])
# tiempo3 = time() - tiempo3
# print("Actividad 3: "+str(float(actividad3)))
# print("Tiempo de la actividad 3: "+str(tiempo3))

print("Tiempo total: "+str(tiempo+tiempo2+tiempo3))