"""
        Archivo: Problema2.py
        Cacculamos el valor de n ingresando 3 valores por teclado
"""

#pedimos datos por teclado
x = input("Ingrese el valor de la variable X");
y = input("Ingrese el valor de la variable Y");
z = input("Ingrese el valor de la variable Z");


#calculamos numeroador y demomiador
numerador =  float(x) + ( float(y) / float(z) );
denominador = float(x) - ( float(y) / float(z) );

#calculamois m
m = numerador / denominador;

#imprimimos los reultado
print("El valor de m, en base a las variables:\nX=%s\n Y=%s\n  Z=%s\nda como resultado:\n\t%.2f"% (x, y, z ,m ))