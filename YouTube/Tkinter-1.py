import tkinter 
#Para crear la ventana: 
ventana = tkinter.Tk()
#Para redimencionar la ventada (Alto y Ancho):
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg="YELLOW") #para agregar en el panel 
#(bg es el color del background).
etiqueta.pack(fill=tkinter.X) #texto centrado (entre el parentesis se puara agregar 
'''la posición deseada (side= thinter.RIGHT)) y el fill rellena el espacio de la etiqueta, otro es 
(fill = tkinter.BOTH, expand = True o 1) para rellenar todo el cuadro de trabajo.'''

def saludo(nombre):
    print("Hola " + nombre)

#crear botones
'''Funcion lambda sirve adicionalmente para agregar parametros o bien para definir 
una función simple a una linea.'''
boton1 = tkinter.Button (ventana, text = "Click", padx=30, pady=40, bg="purple", font= "Helvetica 20" ,command = lambda: saludo("Python"))
boton1.pack(side=tkinter.RIGHT)

def textoDeLaCaja1():
    tex20 = cajaTexto.get()
    print(tex20)

#crear caja de texto
cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()

boton2 = tkinter.Button (ventana, text="Guardar", command = textoDeLaCaja1)
boton2.pack()

def textoDeLaCaja2():
    text21 = cajaTexto.get()
    etiqueta["text"]=text21

boton3 = tkinter.Button (ventana, text="Print", padx=30, pady=40, bg="red", font= "Helvetica 20", command = textoDeLaCaja2)
boton3.pack(side=tkinter.LEFT)

'''Metodo Grid por filas y columnas solo se puede usar desde el inicio
boton4 = tkinter.Button(ventana, text = "Boton 4", padx= 15, pady=15)
boton5 = tkinter.Button(ventana, text = "Boton 5")
boton6 = tkinter.Button(ventana, text = "Boton 6")

boton4.grid(row=0, column=0)
boton5.grid(row=1, column=1)
boton6.grid(row=2, column=2)'''

#Lleva el registro de lo que sucede en la ventana: 
ventana.mainloop()
