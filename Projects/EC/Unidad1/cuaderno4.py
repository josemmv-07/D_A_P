
#  Ejercicio 1: Escribe tres expresiones numéricas: una que utilice enteros, otra con números decimales, y otra con una mezcla de ambos. Muestra los resultados de estas expresiones.

z = 10
x = 1.2

c = z + x
print(c)

#  Ejercicio 2: Crea cadenas utilizando comillas simples, dobles y triples. Muestra cómo funcionan y cuándo es conveniente usarlas. Pregunta: ¿Qué pasa si usas comillas dobles dentro de comillas dobles o comillas simples dentro de comillas simples?

t = "hola", 'Mundo', '''hola '''
print(t)
print("¿Qué pasa si usas comillas dobles dentro de comillas dobles o comillas simples dentro de comillas simples? que te da error")

#  Ejercicio 3: Muestra cómo insertar caracteres especiales, como el salto de línea (\n), tabulación (\t), y comillas dentro de cadenas. Pregunta: ¿Qué efecto tiene cada uno de los caracteres especiales?

print("Hola Mundo\n" 
      "jose\t \"HOLA\"") # \n es salto de linea, \t tabulamos el texto, \" podemos poner comilla sin cerrarla 

#  Ejercicio 4: Demuestra cómo insertar valores en cadenas utilizando f-strings, .format(), y el operador %. Pregunta: ¿Cuál de estos métodos te parece más sencillo de usar? ¿Por qué?

o = "jose"
a = 56.1287

print("Hola me llamo {} y tengo {} años".format(o, a)) 
print("Hola me llamo %s" %o)
print(f"Hola me llamo {o} y tengo {a} años de edad") # me parece mejor f-strings por que es mucho mas rapido y mas sencillo

# Ejercicio 5: Emplea la alineación de texto en cadenas para alinear valores a la izquierda, derecha o centrados. Utiliza .format() o f-strings. Pregunta: ¿Cómo puedes cambiar la alineación de las columnas usando los métodos vistos?

print(f"|{o:<20}|") # a la izquierdad
print(f"|{o:>20}|") # a la derecha
print(f"|{o:^20}|") # centrado

# Ejercicio 6: Realiza ejemplos de formatos de texto con números decimales, enteros, y porcentajes. Usa f-strings o .format(). Pregunta: 
# ¿Cómo puedes redondear el precio a un número específico de decimales? ¿Cómo puedes mostrar un número como porcentaje?

print(f"{a:.2f}")
print(f"{a:.2%}")
print(f"{a=}")

# Ejercicio 7: Solicita el nombre del usuario y muéstralo en pantalla.

nombre = input("¿ cómo te llamas ?\n")
print(f"Tú nombre es {nombre}")

# Ejercicio 8: Solicita al usuario dos números, realiza operaciones matemáticas con ellos y muestra el resultado.

g = int(input("Dime un número\n"))
h = int(input("Dime un número\n"))

print(f"Tu número {g} + {h} = {g + h}")

#  Ejercicio 9: Solicita al usuario que introduzca varios números separados por comas, 
# luego convierte esa entrada en una lista de números y muestra la suma de esos números (emplea la función 'sum').

entrada = input("Introducir números separados por comas: ")
numeros = entrada.split(',')  # Separa cada valor utilizando la coma como caracter separador
# Convertimos cada valor a entero, eliminando posibles espacios en blanco
numeros = [int(num.strip()) for num in numeros]
print("Lista de números:", numeros)
suma = sum(numeros)
print("La suma es:", suma)

# Ejercicio 10: Solicita al usuario una frase y convierte esa frase en una lista de palabras. Luego, muestra la longitud de la lista 
# y la palabra más larga. Emplea la función 'max(palabras, key=len)'.
usua = input("dime una franse")
usus = usua.split()
print(usus)
print(max(usus, key=len))

#  Ejercicio 11: Formatear la salida de una tabla. Solicita al usuario varias entradas para crear una tabla de datos. Por ejemplo, nombre, 
# edad y ciudad, y luego alinea las columnas.

no = input("Nombre:\n")
eda = input("Edad:\n")
ciud = input("Ciudad:\n")
barra = "_"
print(f"{barra:_>20}")
print(f"|Nombre|{no:^13}|", end="")
print(f"|{barra:_>20}|")
print(f"|Edad|{eda:^15}|", end="")
print(f"|{barra:_>20}|")
print(f"|Ciudad|{ciud:^13}|", end="")
print(f"|{barra:_>20}|")





# Ejercicio 12: Cálculo de una media. Solicita al usuario una lista de números separados por comas, luego calcula y muestra la media de esos números. 
# Emplea las funciones 'sum' y 'len' para calcular la media.