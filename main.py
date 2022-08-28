

class Alumno :
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrarDatos(self):
        print("El nombre del alumno es", self.nombre, "su calificación es", self.nota)

    def aprobado(self):
        if self.nota >=7:
            print("El alumno", self.nombre,"ha aprobado.")
        else:
            print("El alumno", self.nombre, "no ha aprobado.")

miAlumno = Alumno("Hernan", 5)
miAlumno.mostrarDatos()
miAlumno.aprobado()