from Arista import *

class Grafo:
    def __init__(self):
        self.aristas = []
        self.libros = {}
        
    def agregar_libro(self, libro):
        self.libros[libro.id] = libro
        
    def agregar_aristas(self, nodo):
        for i in range(len(self.libros)):
            peso = 0
            if nodo.id == self.libros[i].id:
                continue
            #si los libros estan en un rango de +-10 años de publicacion se el suma 1 al peso
            if (nodo.año_publicacion > self.libros[i].año_publicacion - 10) & (nodo.año_publicacion < self.libros[i].año_publicacion + 10):
                peso += 1
            #si los libros coinciden en el genero se le suma 2 al peso
            if nodo.genero == self.libros[i].genero:
                peso += 2
            #si los libros coinciden en el veces prestadas se le suma 2 al peso
            if nodo.veces_prestado == self.libros[i].veces_prestado:
                peso += 2
            #si los libros coinciden en el autor se le suma 3 al peso
            if nodo.autor == self.libros[i].autor:
                peso += 3
            
            arista = Arista(nodo, self.libro[i], peso)
            self.aristas.append(arista)
        
    def __str__(self):
        return f'ARISTA : [{self.nodo_inicio} <--> {self.nodo_destino}:: w:{self.peso}]'