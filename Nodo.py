class Nodo:

    def __init__(self, id, nombre, autor, año_publicacion, genero, veces_prestado):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero
        self.veces_prestado = veces_prestado

    def __str__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Autor: {self.autor} - Año de publicación: {self.año_publicacion} - Género: {self.genero} - Veces prestado: {self.veces_prestado}"