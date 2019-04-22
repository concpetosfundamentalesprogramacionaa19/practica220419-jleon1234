"""
        archivo: problema1.py
        Calculamos el valor  a pagar de un trabajador depende el numero de horas trabjadas
"""
#pedimos por teclado lso datos
nombre = input("Ingrese el nombre del trabajador \n");
horasTrabajadas = input("Ingrese las horas Trabajadas\n");
precioHoras = input("Ingrese el precio por horas");


#Hacemos los calculos del sueldo y del descuento
sueldo = float(horasTrabajadas) * float(precioHoras);
descuento = sueldo * 0.10;
sueldoPagar = sueldo - descuento;

#imprimimos los resultados
print("El valor a pagar a %s es de %.2f" % (nombre, sueldoPagar));