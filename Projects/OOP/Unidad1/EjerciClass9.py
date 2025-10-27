
"""Crea una clase llamada Despedida que modele el comportamiento de una despedida personalizada. Requisitos:

Constructor (__init__). Debe recibir los siguientes parámetros:

nombre: nombre de la persona a la que se dirige la despedida.

hora: (opcional) la hora actual en formato 24h (por defecto 12).

Guarda ambos valores como atributos de instancia.

Método de instancia mostrar_despedida()

Devuelve un mensaje de despedida diferente según la hora del día:

Si la hora es menor de 12 → "¡Que tengas una excelente mañana, <nombre>!"

Si la hora está entre 12 y 21 → "¡Que tengas una buena tarde, <nombre>!"

Si la hora es mayor o igual a 21 → "¡Que tengas una buena noche, <nombre>!"

Método de clase desde_texto(cls, texto)

Recibe una cadena con formato "nombre,hora".

Crea y devuelve una nueva instancia de la clase Despedida a partir de dicha cadena.

Método estático es_hora_valida(hora)

Devuelve True si la hora está en el rango 0 a 23, y False en caso contrario."""

class Despidida:
    pass
