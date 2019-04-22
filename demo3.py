"""
	archivo: demo3.py
	pide desde el teclado dos numeros para hacer suma y multiplicacion
"""
valor1 = input("Ingrese el primer numero ")
valor2 = input("Ingrese el segundo numero ")

suma = int(valor1) + int(valor2)
multiplicacion = int(valor1) * int(valor2)

print("La suma es: %s \nLa multiplicacion es: %s " % (suma, multiplicacion))
