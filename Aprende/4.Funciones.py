# Funciones
# Cálculo de Áreas
F = 3.141516

# Área del Cuadrado
def acuadrado():
    lado = int(input("¿Cuál es el valor del lado? "))
    x = lado ** 2
    print("El área del cuadrado es", x, "unidades cuadradas\n")

# Área del Triángulo
def atriangulo():
    base = int(input("¿Cuál es el valor de la base? "))
    altura = int(input("¿Cuál es el valor de la altura? "))
    y = (base * altura) / 2
    print("El área del triángulo es", y, "unidades cuadradas\n")

# Área del Círculo
def acirculo():
    radio = int(input("¿Cuál es el valor del radio? "))
    z = (F * radio) ** 2
    print("El área del círculo es", z, "unidades cuadradas\n")

# Función para preguntar si desea calcular otra figura
def otra_consulta():
    respuesta = input("\n¿Quieres calcular el área de otra figura? (Sí/No): ").lower()
    return respuesta == "sí" or respuesta == "si"

# Bucle principal
while True:
    area = int(input("Elige la figura geométrica para calcular su área:\n1. Cuadrado\n2. Triángulo\n3. Círculo\n"))
    if area == 1:
        acuadrado()
    elif area == 2:
        atriangulo()
    elif area == 3:
        acirculo()
    else:
        print("Ingresa una opción válida")

    if not otra_consulta():
        break

'''
#Calculo de Areas
F=3.141516
#Area del Cuadrado
def acuadrado():
    lado = int(input("Cual es el valor del lado? "))
    x = lado**2
    print("El area del cuadrado es", x, "unidades cuadradas\n")
#Area del triangulo
def atriangulo():
    base = int(input("Cual es el valor de la base? "))
    altura = int(input("Cual es le valor de la altura? "))
    y = base * altura / 2
    print("El area del triangulo es", y, "unidades cuadradas\n")
#Area del Circulo
def acirculo():
    radio = int(input("Cual es el valor del radio "))
    z = (F * radio) ** 2
    print("El area del circulo es", z, "unidades cuadradas\n")

i = True
while i == True:
    area = int(input("Elije la figura geometrica para calcular su area \nCuadrado = 1 \nTriangulo = 2 \nCirculo = 3\n"))
    if area==1:
        acuadrado()
    elif area==2:
        atriangulo()
    elif area==3:
        acirculo()
    else:
        print("Ingresa una opción valida")

    i = (input("\nQuieres calcular el area de otra figura?\n Si=True \nNo=False\n"))

Fuciones: es un conjunto de lineas de código que pueden ser reutilizables y
sirven para organizar un programa en forma de bloques cortos 
Estructura: def prueba(numero): def: instrucción + prueba: nombre de la función +
(numero): y entre parentesis las variables necesarias para el proceso'''