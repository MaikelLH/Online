#Operaciones Basicas con Archivos: Crear, Escribir y Leer Lineas de Codigo.
'''Sintaxis: Variable = instrucción OPEN (abre el archivo) + Ruta y nombre del
archivo a usar con su extensión, "r (read) o w(write)
Permite trabajar con datos de otras extensiones inclusive inportar datos'''

def  escritura (datoa, datob, datoc):
    prueba=open('"C:\Users\Maike\Python\Python_VS\Aprende\OperacionesBasicas.py"','w')
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print ("escritura")
    prueba.close
escritura('Hola', 
          'Mundo',
          'Bonito')
def lectura():
    prueba=open('"C:\Users\Maike\Python\Python_VS\Aprende\OperacionesBasicas.py"','r')
    print(prueba.read())
    prueba.close
    lectura()
