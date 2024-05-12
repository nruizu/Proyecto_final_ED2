from Grafo import *
from Nodo import *
from Persona import *

def agregar_personas():
    personas = []
    personas.append(Persona("Juan", "El señor de los anillos"))
    personas.append(Persona("Pedro", "Harry Potter y la piedra filosofal"))
    personas.append(Persona("Ana", "El código Da Vinci"))
    personas.append(Persona("María", "El alquimista"))
    personas.append(Persona("Carlos", "El principito"))
    personas.append(Persona("Luis", "Cien años de soledad"))
    personas.append(Persona("Sofía", "Don Quijote de la Mancha"))
    personas.append(Persona("Lucía", "El retrato de Dorian Gray"))
    personas.append(Persona("Marta", "La Odisea"))
    personas.append( Persona("José", "La Ilíada"))
    return personas

def agregar_libros():
    grafo = Grafo()

    libro1 = Nodo(1, "El señor de los anillos", "J.R.R. Tolkien", 1954, "Fantasía")
    libro2 = Nodo(2, "Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Fantasía")
    libro3 = Nodo(3, "El código Da Vinci", "Dan Brown", 2003, "Misterio")
    libro4 = Nodo(4, "El alquimista", "Paulo Coelho", 1988, "Novela")
    libro5 = Nodo(5, "El principito", "Antoine de Saint-Exupéry", 1943, "Fábula")
    libro6 = Nodo(6, "Cien años de soledad", "Gabriel García Márquez", 1967, "Novela")
    libro7 = Nodo(7, "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela")
    libro8 = Nodo(8, "El retrato de Dorian Gray", "Oscar Wilde", 1890, "Novela")
    libro9 = Nodo(9, "La Odisea", "Homero", -800., "Épico")
    libro10 = Nodo(10, "La Ilíada", "Homero", -800, "Épico")

    grafo.agregar_libro(libro1)
    grafo.agregar_libro(libro2)
    grafo.agregar_libro(libro3)
    grafo.agregar_libro(libro4)
    grafo.agregar_libro(libro5)
    grafo.agregar_libro(libro6)
    grafo.agregar_libro(libro7)
    grafo.agregar_libro(libro8)
    grafo.agregar_libro(libro9)
    grafo.agregar_libro(libro10)
    return grafo

if __name__ == "__main__":
    personas = agregar_personas()
    grafo = agregar_libros()

    