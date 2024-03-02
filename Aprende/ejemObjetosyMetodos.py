class Persona:
    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def hablar (self, palabras = "No se que decir"):
        print (self.nombre, ': ', palabras)

Juan = Persona()
Juan.hablar()
Juan.hablar("Hola, estoy hablando")

'''Objeto: metodología que permite organizar la información de acuerdo a la
interacción de entidades.
1. Representación informática de un objeto físico o imaginario.
2. Puede ser simple o complejo.
3. Dependiendo de la dimensión de sus tres propiedades: Estado,
Comportamiento e Identidad.
    Estado: está definido por un conjunto de datos llamados: Atributos que
        almacenan las características del objeto en determinado momento.
    Comportamiento: está definido por sus métodos, estos son funciones que
        permiten su interacción con el programa y otros objetos.
    Identidad: se define por medio del identificador con el que se declara.
4. Propiedades Adicionales: extienden las funciones de un objeto: Herencia,
Abstracción, Encapsulamiento - permite al programador crear sistema más grandes
y mejor estructurados aprovechando la reutilización del código.
5. Todas las propiedades mencionadas se definen a través de plantillas llamadas "Clases" -
Son instancias que poseen las características esenciales definidas en su clase.
   
Objetos y Declaración de Clases: primero se debe crear la plantilla de su clase a este
proceso se le llama "Declaración de Clase" que es similar a la declaración de funciones.

1. Palabra reservada: class
2. Nombre de la clase: se debe escribir en letras minusculas y la primer letra en mayuscula.
3. Atributos: se declaran dentro de un método especial que se ejecuta automaticamente al declarar
un objeto y se le llama "Método Constructor" y tiene una sintaxis especial reservada.
4. Palabra Self es necesaria para acceder al resto de los métodos y atributos dentro de la clase
por eso debe ser el primer parametro de todos los metodos de clase y es de uso exclusivo de Python.

Uso de Métodos: son funciones declaradas dentro de una clase que sirven para interactuar con ella

Atributos:
class Persona:
    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print ("Se ha creado a", self.nombre, "de",self.edad)

Métodos:         
    def hablar (self, palabras = "No se que decir"): varlor predeterminado
        print (self.nombre, ': ', palabras)

Juan = Persona()
Juan.hablar()
Juan.hablar("Hola, estoy hablando") valor definido        

Parámetros Especiales: el constructor tambien puede incluir parámetros en su 
defición conocidos como "variables de instancia":

class Persona:
    def __init__(self, edad, nombre): variables de instancia
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def hablar (self,*palabras):
        for frase in palabras:
            print (self.nombre, ': ', frase)

Instancias (instanciar): al instanciar un objeto se está ejecutando 
de forma automatica el método constructor.

Juan = Persona(30, "Juan")
Juan.hablar()
Juan.hablar("Hola, estoy hablando", "Este soy Yo")
Luis = Persona(18, "Luis")
Luis.hablar ()
Luis.hablar ("Hola, estoy hablando", "Este soy Yo")

Tuplas: agegar asterisco e iniciar el ciclo for:

class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def hablar (self,*palabras): tupla
        for frase in palabras:
            print (self.nombre, ': ', frase)

Juan = Persona(30, "Juan")
Juan.hablar()
Juan.hablar("Hola, estoy hablando", "Este soy Yo")
Luis = Persona(18, "Luis")
Luis.hablar ()
Luis.hablar ("Hola, estoy hablando", "Este soy Yo")

Dicionarios: agregar dos asteriscos para indicar que recibira un
diccionario como valor y usar corchetes.

class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def hablar (self,**palabras): dicionarios
        for frase in palabras:
            print (self.nombre, ': ', palabras[frase])

Juan = Persona(30, "Juan")
Juan.hablar()
Juan.hablar(t1= "Hola, estoy hablando", t2= "Este soy Yo")
Luis = Persona(18, "Luis")
Luis.hablar ()
Luis.hablar (t1= "Hola, estoy hablando", t2= "Este soy Yo")


****La Variable que se use para recibir Tuplas, Listas, Diccionarios
siempre debe declararse como el último parámetro así Python sabra que 
el resto de los valores pasados como parámetro forman parte de la tupla****

Los Métodos sirven para realizar operaciones dentro del objeto y para 
interactuar con el programa principal y otros objetos

'''
