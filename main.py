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

def crear_grafo():
    grafo = Grafo()

    libro1 = Nodo(1, "El señor de los anillos", "J.R.R. Tolkien", 1954, "Fantasía", 5)
    libro2 = Nodo(2, "Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Fantasía", 10)
    libro3 = Nodo(3, "El código Da Vinci", "Dan Brown", 2003, "Misterio", 15)
    libro4 = Nodo(4, "El alquimista", "Paulo Coelho", 1988, "Novela", 3)
    libro5 = Nodo(5, "Harry Potter y la cámara secreta", "J.K. Rowling", 1998, "Fantasía", 10)
    libro6 = Nodo(6, "Cien años de soledad", "Gabriel García Márquez", 1967, "Novela", 1)
    libro7 = Nodo(7, "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela",6)
    libro8 = Nodo(8, "El retrato de Dorian Gray", "Oscar Wilde", 1890, "Novela", 4)
    libro9 = Nodo(9, "La Odisea", "Homero", -800., "Épico",6)
    libro10 = Nodo(10, "La Ilíada", "Homero", -800, "Épico", 3)

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

    grafo.agregar_aristas(libro1)
    grafo.agregar_aristas(libro2)
    grafo.agregar_aristas(libro3)
    grafo.agregar_aristas(libro4)
    grafo.agregar_aristas(libro5)
    grafo.agregar_aristas(libro6)
    grafo.agregar_aristas(libro7)
    grafo.agregar_aristas(libro8)
    grafo.agregar_aristas(libro9)
    grafo.agregar_aristas(libro10)
    return grafo

def comparar_peso(a):
    return a.peso


if __name__ == "__main__":
    personas = agregar_personas()
    grafo = crear_grafo()

    persona = input("Ingrese su nombre: ")

    for x in personas:
        if x.nombre_persona == persona:
            persona = x
            break

    lended_book = persona.libro_prestado
    for i in grafo.libros.values():
        if i.nombre == lended_book:
            lended_book = i
            break

    recomendaciones = []
    for i in grafo.aristas:
        #si el peso es 0 no se recomienda ya que no estan relacionados
        if i.peso == 0:
            continue
        if i.origen == lended_book:
            recomendaciones.append(i)

    recomendaciones.sort(key=comparar_peso)
    recomendaciones.reverse()

    print("Te podrian interesar los siguientes libros: ")
    cont = 1
    for i in recomendaciones:
        print(f"{cont}. {i.destino}\n")
        cont +=1