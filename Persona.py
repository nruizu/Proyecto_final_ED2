class Persona:
    def __init__(self, nombre_persona, libro_prestado):
        self.nombre_persona = nombre_persona
        self.libro_prestado = libro_prestado

    def __str__(self):
        return f'Nombre: {self.nombre} - Presto: {self.libro_prestado} '