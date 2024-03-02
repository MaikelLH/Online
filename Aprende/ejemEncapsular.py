#Encapsulamiento y Ocultación en objetos 
'''Modificaciones de acceso o palabras reservadas que restringen la info en 3 niveles:
Pública, Protegida y Privada -> la ocultación de atributos y metodos se realiza agregando
dos guiones bajos al inicio de su identificador (encapsular)
'''
#Superclase
class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def hablar (self,*palabras):
        for frase in palabras:
            print (self.nombre, ': ', frase)

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


Juan = Persona(30, "Juan")
Juan.hablar()
Juan.hablar("Hola, estoy hablando", "Este soy Yo")
Luis = Deportista(18, "Luis", "natación")
Luis.hablar ()
Luis.hablar ("Hola, estoy hablando", "Este soy Yo")
Luis.practicarDeporte()
print ("Luis Practica", Luis.verMiDeporte())