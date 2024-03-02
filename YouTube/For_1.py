#Bucle For
print ("Inicio de Ejecicio #1)")
#Ejercicio 1: recorre el print elemento por elemento - la cantidad de veces de la colección.
for i in [1,2,3,4,5]:
    print ("Hola Mundo")
print ("Fin de Ejecicio #1)")

#Ejercicio 2: recorre el print elemento por elemento - la cantidad de veces de la colección, no importa lo que diga la colección.
print ("Inicio de Ejecicio #2)")
for i in [70,2,"Maikel",4,"Loana"]:
    print ("Hola Mundo")
print ("Fin de Ejecicio #2)")

#Ejercicio 3: Mostrar el valor de la variable iteradora
print ("Inicio de Ejecicio #3)")
for i in [70,2,"Maikel",4,"Loana"]:
    print (f"Elemento: {i}")
print ("Fin de Ejecicio #3)")

#Ejercicio 4: Se puede poner directamente en la colección o como variable exterior
print ("Inicio de Ejecicio #4: Colección")
coleccion = [70,2,"Maikel",4,"Loana"]
for i in coleccion:
    print (f"Elemento: {i}")
print ("Fin de Ejecicio #4)")

#Ejercicio 5: con lista
print ("Inicio de Ejecicio #5: Lista)")
lista = [70,2,"Maikel",4,"Loana"]
for i in lista:
    print (f"Elemento: {i}")
print ("Fin de Ejecicio #5)")

#Ejercicio 6: tuplas
print ("Inicio de Ejecicio #6: Tuplas)")
tuplas = (70,2,"Maikel",4,"Loana")
for i in tuplas:
    print (f"Elemento: {i}")
print ("Fin de Ejecicio #6)")

#Ejercicio 7: conjuntos
print ("Inicio de Ejecicio #7: Conjunto)")
conjunto = {70,2,"Maikel",4,"Loana"}
for i in conjunto:
    print (f"Elemento: {i}")
print ("Fin de Ejecicio #7)")

#Ejercicio 8: diccionarios (clave)
print ("Inicio de Ejecicio #8: Diccionario Solo Clave)")
diccionario = {"Loana": 10, "Daniela": 39, "Maikel": 41, "Zoe": 2, "Susy": 6}
for i in diccionario:
    print (f"Elemento: {i}")
print ("Fin de Ejecicio #8)")

#Ejercicio 9: diccionarios (Valor)
print ("Inicio de Ejecicio #9: Diccionario Solo Valor")
diccionario = {"Loana": 10, "Daniela": 39, "Maikel": 41, "Zoe": 2, "Susy": 6}
for i in diccionario:
    print (f"Elemento: {diccionario[i]}")
print ("Fin de Ejecicio #9)")

#Ejercicio 10: diccionarios (Clave + Valor)
print ("Inicio de Ejecicio #10: Diccionario Clave + Valor")
diccionario = {"Loana": 10, "Daniela": 39, "Maikel": 41, "Zoe": 2, "Susy": 6}
for i in diccionario:
    print (f"{i} Edad: {diccionario[i]}")
print ("Fin de Ejecicio #10)")

#Ejercicio 11: usar dos variables iteradoras con el metodo Items
print ("Inicio de Ejecicio #11: Diccionario Clave + Valor con dos Iteraciones")
diccionario = {"Loana": 10, "Daniela": 39, "Maikel": 41, "Zoe": 2, "Susy": 6}
for clave,valor in diccionario.items():
    print (f"{clave} Edad: {valor}")
print ("Fin de Ejecicio #11")

#Ejercicio 12: Recorrer cadenas
print ("Inicio de Ejecicio #12: Recorrer Cadenas")
diccionario = {"Loana": 10, "Daniela": 39, "Maikel": 41, "Zoe": 2, "Susy": 6}
for clave,valor in diccionario.items():
    print (f"{clave} Edad: {valor}")
print ("Fin de Ejecicio #11")



'''
-Usa un número determinado de iteraciones
-Un iterador que va a recorrer los elementos de una colección:
Lista, Tupla, Conjunto, Diccionario, Cadena
-Se va a repetir como tantos elementos tengas en 
la colección'''


