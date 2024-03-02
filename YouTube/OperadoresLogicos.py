#Operadores Lógicos

a = 10
b = 15
c = 20

resultado = ((a<b) and (b<c))
print(resultado)

resultado = ((a>b) or (b<c))
print(resultado)

resultado = not((a>b) or (b<c))
print(resultado)

'''
-Permite construir expresiones lógicas, se obtiene como resultado booleanos.
-Prioridad: 1. not, 2. and y 3. or
True es igual a 1 (Operando1) y False es igual a 0 (Operando2):

And (Conjunción) palabra reservada: and "Se conoce como una multiplicación lógica"
los dos deben ser verdadero para que sea True:
True and True = True
True and False = False
False and True = False
False and False = False

Or (Disyunción) palabra reservada: or "Se conoce como una suma lógica" 
con solo un verdadero el valor va a dar True:
True or True = True
True or False = True
False or True = True
False or False = False

Not (Negación) palabra reservada: not
si tienes un verdadero resultado va a dar False o alreves:
not(True) = False
not(False) = True

Prioridades en General:
1. ()
2. **
3. *, /, mod, not
4. +, -, and
5 >, <, ==, >=, <=, !=, or

'''