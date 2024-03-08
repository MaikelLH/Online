#Tabla del 7 usando While
print("Ciclo Usando While")
i = 0
while i <= 9:
    i += 1
    tabla = 7*i
    print("7 x", (i), "=", (tabla))

#Tabla del 7 usando While
print("Ciclo Usando For")
for j in range(0,10):
    j=j+1
    print("7 x", (j), "=", (j*7))

#For lectura de elementos en lista incluyendo palabras.
print("Lectura de elementos con For")
for palabras in "Maikel LH":
    print(palabras)
