import math
#Ejercicio 1
for i in range (5):
    print('Hola Mundo')

#Ejercicio 2
'''Crear un programa modular que calcule el área de un triángulo valores 
de entrada por teclado.'''
def calcularArea(a, b):
    area = (b * a) / 2
    return area

print("Ingresar altura")
a = float(input())
print("Ingresar base")
b = float(input())

print("El Área del Triangulo es " + str(calcularArea(a, b)))

#Ejercio 3
#Crear un programa que calcule el área de un circulo.
def calcularAreaCirculo(r):
    area = math.pi * math.pow(r, 2)
    return area

print("Ingresar Radio del Círculo")
r = float(input())

print("El Área del Círulo es " + str(calcularAreaCirculo(r)))

#Ejercicio 4
'''Programa modular que calcule la edad dado el año, el año debe 
leer por el usario atraves del teclado'''
def calcularEdad(nac, actual):
    edad = actual - nac
    return edad

print("Ingrese año de Nacimiento")
nac = int(input())
print("Ingrese año actual")
actual = int(input())

print("Su Edad es " + str(calcularEdad(nac, actual)))