#  Ejercicio 1.1: Crea una variable llamada edad y asigna tu edad como valor. Luego, usa la función type() para verificar el tipo de la variable.

edad = 28
print(type(edad))

#  Ejercicio 1.2: Crea una variable llamada nombre y asigna tu nombre como valor. ¿De qué tipo es esta variable? Utiliza type() para verificarlo.

nombre = "Jose"
print(type(nombre))

# Ejercicio 1.3: Asigna el valor True a una variable llamada es_estudiante. Usa la función type() para confirmar su tipo.

es_estudiante = True
print(type(es_estudiante))

#  Ejercicio 1.4: Crea una variable pi y asígnale el valor de pi con una precisión de 3 decimales (de forma manual). ¿Qué tipo tiene esta variable?

pi = 3.142
print(type(pi))

# Ejercicio 1.5: Crea una variable temperatura y asigna el valor 25. Usa del() para eliminar la variable y luego intenta imprimirla. ¿Qué error aparece?

temperatura = 25
del(temperatura)
# print(temperatura)

# Ejercicio 1.6: Crea tres variables 'x', 'y', 'z' y asígnales valores. Luego, elimina la variable 'y' usando del() y verifica si puedes imprimir su valor.

x = 3
y = 54
z = 45
del(y)
print(x)
#print(y)
print(z)

# Ejercicio 2.1: Crea una variable que siga las siguientes reglas: empieza con una letra, contiene un número y no tiene caracteres especiales (p.ej., _, #, etc.)

a4 = 34
print(a4)

# Ejercicio 2.2: Intenta crear una variable con un nombre que empiece con un número. ¿Qué error aparece?


# 4r = 45   File "c:\Users\jmorval1009b\Projects\EC\Unidad1\cuaderno3.py", line 43
#SyntaxError: invalid decimal literalPS C:\Users\jmorval1009b\Projects>


# Ejercicio 2.3: Crea una variable con un nombre largo que use letras y guiones bajos.

clase_del_cole = "clase"
print(clase_del_cole)

# - Ejercicio 2.4: Intenta crear una variable con un nombre que sea una palabra reservada en Python (por ejemplo, if, else, for). ¿Qué error aparece?

# if = "Hola"   File "c:\Users\jmorval1009b\Projects\EC\Unidad1\cuaderno3.py", line 56if = "Hola"^SyntaxError: invalid syntax

# Ejercicio 2.5: Crea un listado de al menos 5 palabras reservadas en Python y escribe brevemente qué hacen (puedes buscar en la documentación).

x = 10 # Un número entero
y = 3.14 # Un número decimal
z = "Hola" # Una cadena de texto
a = True # Un valor lógico
b = None # Un valor nulo

# Ejercicio 3.1: Asigna a la variable 'a' el valor 10, a la variable 'b' el valor 5 y luego realiza una operación matemática entre ellas (suma, resta, multiplicación, etc.) y almacena el resultado en una nueva variable llamada resultado.

a = 10
b = 5

resultado = a + b
print(resultado)

resultado = a * b
print(resultado)

resultado = (a - b)
print(resultado)

# - Ejercicio 3.2: Crea tres variables, x = 10, y = 20 y z = 30. Luego, asigna a la variable total la suma de estas tres variables

x = 10
y = 20
z = 30
total = x + y + z

print(total)

# - Ejercicio 3.3: Crea una variable 'ninguno' y asígnale el valor None. ¿Qué tipo tiene esta variable?

p = None
print(type(p)) # NoneType

# Ejercicio 4.1: Imprime en pantalla los valores de dos variables: nombre = "Ana" y edad = 25. La salida debería verse así: "Ana tiene 25 años".

nombre = "Ana"
edad = 25
print(nombre, "tiene", edad, "años")

# Ejercicio 4.2: Usa el argumento end para que la función print imprima "Hola" y luego "Mundo" en la misma línea, separadas por un espacio.

print("Hola", end=" ")
print("Mundo")

# Ejercicio 4.3: Usa el argumento sep para imprimir los valores 1, 2 y 3 con un guion (-) como separador entre ellos.

print(1, 2, 3, sep="-")

# - Ejercicio 4.4: Imprime las palabras "Python", "es", "genial" en la misma línea, pero separadas por comas.

print("Python", "es", "genial", sep=",")

#  Ejercicio 5.1: Crea un programa que pida al usuario su nombre y su edad, los guarde en variables y luego imprima un mensaje que diga "Hola, [nombre]. Tienes [edad] años". Escribe un comentario de una sola línea que describa el propósito de tu código.

a = input("¿como te llamas?\n")
b = input("¿Qué edad tienes?\n")

print(f"Hola, {a}. Tienes {b} años.") # llama a la variable a y b que esta dentro de un input

# Ejercicio 5.2: Crea tres variables: una con un valor booleano, otra con un número y otra con una cadena de texto. 
# Usa print() para mostrar los tres valores en una sola línea, separados por un guion. Escribe un comentario de varias 
# líneas en el que expliques qué hace el código.

a = True
b = 10
c = "Hola Mundo"

print(a,b,c, sep="-")
"""El codigo imprime a que es verdadero\
    que b es un entero y c una cadena de texto"""

# - Ejercicio 5.3: Realiza una operación matemática con variables que hayas asignado anteriormente y usa print() 
# para mostrar el resultado de la operación. Comenta temporalmente una línea de código que imprima un valor para evitar que se ejecute.

print(x + y + z)