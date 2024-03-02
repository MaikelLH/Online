# Bucle While

import math

numero = int(input("Digite un Número: "))

while numero<0:
    print("Error -> Deberia ser un Número Positivo")
    numero = int(input("Digite un Número: "))

print(f"\nSu Raiz Cuadrada es: {(math.sqrt(numero)):.2f}")

'''Mientras se siga cumpliendo la condicion
el bucle se sigue ejecutando - Cuando deja 
de cumplirse se sale del bucle (no ejecuta el 
while sí la condición del mismo no entra para 
cumplise)'''

#Mostrar 10 veces el mensaje
i = 0
while i<10:
    print("Hola Mundo")
    i += 1
#Mostrar los números hasta cumplir la variable
a = 0
while a<11:
    print(a)
    a += 1
