"""

Crea una clase llamada Curso con las variables de instancia título, instructor, precio, clases, usuarios (tipo lista), calificaciones y calificación promedio. 

Implementa los métodos __str__, new_user_enrolled, received_a_rating y show_details.

 De la clase anterior, hereda las clases VideoCourse y PdfCourse. 

La clase VideoCourse tiene la variable de instancia length_video y PdfCourse tiene la variable de instancia pages.

Muestra por pantalla los datos del curso según su título.
"""

class Curso:

    def __init__(self, título, instructor, precio, clases, usuarios, calificaciones, calificación_promedio):
        self.título = título
        self.instructor = instructor
        self.precio = precio
        self.clases = clases
        self.usuarios = usuarios
        self.calificaciones = calificaciones
        self.calificación_promedio = calificación_promedio
        usuarios = []

        
