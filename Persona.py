class Persona:
    def __init__(self, nombre, libro_prestado):
        self.nombre = nombre
        self.libro_prestado = libro_prestado

    def __str__(self):
        return f'Nombre: {self.nombre} - Presto: {self.libro_prestado} '