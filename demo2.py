"""
	archivo: demo2.py
	pide desde el terminal dos numeros para hacer suma y multiplicacion
"""
import sys

varibale = sys.argv[0]
dato1 = sys.argv[1]
dato2 = sys.argv[2]

suma = int(dato1) + int(dato2)
multiplicacion = int(dato1) * int(dato2)

print("La suma es: %s" % suma)
print("La multiplicacion es: %s" % multiplicacion)