from Arista import *

class Grafo:
    def __init__(self):
        self.aristas = []
        self.libros = {}
        
    def agregar_libro(self, libro):
        self.libros[libro.id] = libro
        
    def agregar_arista(self, origen, destino):
        peso = 0
        #si los libros coinciden en el año de publicacion se el suma 1 al peso
        if origen.año_publicacion == destino.año_publicacion:
            peso += 1
        #si los libros coinciden en el genero se le suma 2 al peso
        if origen.genero == destino.genero:
            peso += 2
        #si los libros coinciden en el veces prestadas se le suma 2 al peso
        if origen.veces_prestado == destino.veces_prestado:
            peso += 2
        #si los libros coinciden en el autor se le suma 3 al peso
        if origen.autor == destino.autor:
            peso += 3
            
        arista = Arista(origen, destino, peso)
        self.aristas.append(arista)
        
    def __str__(self):
        return f'ARISTA : [{self.nodo_inicio} <--> {self.nodo_destino}:: w:{self.peso}]'