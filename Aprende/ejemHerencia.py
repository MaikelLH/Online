#Herencia y Sobreescritura (agregando un init a la nueva clase)
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
        self.deporte = deporte
        print ("Se ha creado a", self.nombre, "de",self.edad)


    def practicarDeporte (self):
        print (self.nombre, ": voy a practicar")

Juan = Persona(30, "Juan")
Juan.hablar()
Juan.hablar("Hola, estoy hablando", "Este soy Yo")
Luis = Deportista(18, "Luis", "natación")
Luis.hablar ()
Luis.hablar ("Hola, estoy hablando", "Este soy Yo")
Luis.practicarDeporte()
print ("Luis Practica", Luis.deporte)