import math
print(math.sqrt(25))  # Raíz cuadrada de 25

print("¡Hola, mundo!")
print(223 + 665 * 67)

nombre = "Ana"
edad = 20

print(nombre)

nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)

edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

for i in range(5):
    print(i)

def saludar(nombre):
    print("¡Hola, " + nombre + "!  Soy tu programa de Python. ¡Que pases un buen día!")

saludar("Pablo")
saludar("Miguel")
saludar("Sandra")

# Esta función suma dos números
def suma(a, b):
    return a + b

print(suma(5, 4))