"""

Desarrollar en lenguaje Python la estructura representada en el siguiente Diagrama de Clases. 

En dicho diagrama se describe la estructura para representar los alumnos de un Ciclo Formativo con sus módulos y calificaciones.

Se deben desarrollar las clases Persona, Alumno, Calificación y Módulo. 

A continuación se describe la funcionalidad de los métodos más importantes: 

En la clase Alumno, el método matricular() añadirá un módulo y su calificación al alumno. 

La calificación inicial será 0, indicando que aún está sin calificar.

El método calificar() servirá para asignarle una calificación numérica (1- 10) al alumno en el módulo especificado. 

Si el alumno ya estaba matriculado de ese módulo, el método no hará nada. 

Los métodos que toman un módulo como argumento, si tienen que buscar dicho módulo entre las calificaciones, usarán el nombre del módulo para determinar la coincidencia. 

El método promociona() devolverá true si el alumno está en condiciones de promocionar, es decir, si la suma de las horas de los módulos aprobados es mayor o igual al 50% del total de horas de los módulos matriculados.

El método toString() de Alumno, devolverá lo mismo que el de Persona (datos personales), añadiendo detrás, “Nota Media = X.XX”, donde X.XX será la nota media del alumno, con dos cifras decimales como máximo.

"""

class Coche(Vehiculo):
  """La clase Coche es subclase de Vehiculo"""

  def __init__(self, marca, modelo, numero_de_puertas=4):
    super().__init__(marca, modelo)
    self.numero_de_puertas = numero_de_puertas

  def __str__(self):
    return f"{super().__str__()} | Nº de puertas: {self.numero_de_puertas}"

  def recorre(self, km):
    super().recorre(km)
    print("¡Estoy quemando gasolina!")

class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

class Modulo:
    pass

class Calificación(Modulo):
    pass

class Alumno(Calificación, Persona):
    def __init__(self, dni, nombre, apellido):
       super().__init__(dni, nombre, apellido)




