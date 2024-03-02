#Diccionario
class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de",self.edad)

    def hablar (self,**palabras):
        for frase in palabras:
            print (self.nombre, ': ', palabras[frase])

Juan = Persona(30, "Juan")
Juan.hablar()
Juan.hablar(t1= "Hola, estoy hablando", t2= "Este soy Yo")
Luis = Persona(18, "Luis")
Luis.hablar ()
Luis.hablar (t1= "Hola, estoy hablando", t2= "Este soy Yo")

