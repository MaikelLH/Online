#Operadores Relacionales

num1 = 20
num2 = 30
num3 = 15

# > Mayor que
Resultado = num1 > num2
print("El Primer Número es Mayor que el Segundo Número:",Resultado)

# < Menor que
Resultado = num1 < num2
print("El Primer Número es Menor que el Segundo Número:",Resultado)

# >= Mayor o Igual que
Resultado = num1 >= num2
print("El Primer Número es Mayor o Igual que el Segundo Número:",Resultado)

# <= Menor o Igual que
Resultado = num1 <= num2
print("El Primer Número es Menor o Igual que el Segundo Número:",Resultado)

# != Diferencia
Resultado = num1 != num2
print("El Primer Número es Diferente al Segundo Número:",Resultado)

# == Igual
Resultado = num1 == num2
print("El Primer Número es Igual al Segundo Número:",Resultado)

# Combinar Operaciones Relaciones y Aritméticos
Resultado = num1+num2 >= num3
print("La Suma del Primer Número más Segundo Número es Mayor que el Tercer Número:",Resultado)

Resultado = num1-num2 == num3
print("La Resta del Primer Número más Segundo Número es Igual que el Tercer Número:",Resultado)

Resultado = num1/num2 > num3
print("La División del Primer Número y Segundo Número es Mayor que el Tercer Número:",Resultado)
'''
-Se utilizan para establecer una relación entre 2 valores
-Compara estos valores entre si y esta comparación produce un resultado
de certeza o falsedad (verdadero o falso)
-Tienen el mismo nivel de prioridad en su evalución (se ejecutan de Izquierda a Derecha)
-Los operadores relacionales tienen menor prioridad que los aritméticos (operadores
aritméticos se ejecutan primero)
> Mayor que
< Menor que
>= Mayor o Igual que
<= Menor o Igual que
!= Diferencia
== Igual
'''