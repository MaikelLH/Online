#Listas: se encierran entre corchetes y sí se pueden modificar
robot = ["bipedo",6,["caminar","correr","saltar"]]
variable1 = robot[1]
print (variable1)

variable1 = robot[2][1]
print (variable1)

print (robot)

#reescribir elementos
robot [2] [1] = "trotar"
print(robot)

#Tuplas: se encierran entre parentesis y no se puede modificar
xy=("Primavera","Verano","Otoño","Invierno")
print (xy[0])

'''.Diccionarios: estructuras que asocian una clave con un valor, se pueden 
cambiar los valores pero No las claves'''
dic = {'Clave1':"Bipedo",'Clave2':6,'Clave3':["caminar","correr","saltar"]}
       
dic2 = dic["Clave3"][1]
print (dic2)

print (dic)