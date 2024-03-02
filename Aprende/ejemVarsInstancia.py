#Variables de Instancia - Metodo Construcctor
class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def hablar (self, palabras = "No se que decir"):
        print (self.nombre, ': ', palabras)       

Juan = Persona(18, "Juan")
Juan.hablar()
Juan.hablar("Hola, estoy hablando")
Luis = Persona (20, "Luis")
Luis.hablar ()
Luis.hablar ("Hola, estoy hablando")


