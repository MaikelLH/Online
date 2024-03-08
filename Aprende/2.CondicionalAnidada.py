pregunta = (input("Trabajas desde Casa "))
if pregunta == "Si":
    print("Eres Afortunado")
    exit()
if pregunta == "No":
    print("Trabajas fuera de casa")

tiempo = int(input("Cuantos minutos haces al trabajo "))
if tiempo ==0:
    print("Trabajas desde Casa")
elif tiempo <= 20:
    print("Es poco tiempo")
elif tiempo >= 21 and tiempo <= 45:
    print("Es un tiempo razonable")
else: 
    print("Busca otras rutas")
