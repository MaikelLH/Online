#Clases abstractas
from abc import ABCMeta,abstractmethod

#Superclase
class Persona:
    __metaclass__ = ABCMeta
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de",self.edad)

    @abstractmethod
    def hablar (self): pass


#SubClase
class Deportista (Persona):
    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte #encapsulado
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def practicarDeporte (self):
        print (self.nombre, ": voy a practicar")
        
#metodo publico que accede al valor oculto por el doble guion o en capsulado
    def verMiDeporte(self):
        return self.__deporte                 

    def hablar(self,*palabras):
        for frase in palabras:
            print (self.nombre, ";", frase)


Luis = Deportista(18, "Luis", "natación")
Luis.hablar ()
Luis.hablar ("Hola, estoy hablando", "Este soy Yo")
Luis.practicarDeporte()
print ("Luis Practica", Luis.verMiDeporte())