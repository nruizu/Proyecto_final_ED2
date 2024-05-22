from Grafo import *
from Nodo import *
from Persona import *
import csv

def agregar_personas():
    personas = []
    with open('personas.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # Saltar la primera fila que contiene los encabezados
        encabezados = next(csv_reader)
        for fila in csv_reader:
            personas.append((Persona(fila[0], fila[1])))

    return personas

def crear_grafo():
    grafo = Grafo()

    with open('libros.csv', mode='r', encoding='utf-8') as f:
        lector_csv = csv.reader(f)
        encabezados = next(lector_csv)
        for fila in lector_csv:
            grafo.agregar_libro(Nodo(int(fila[0]), fila[1], fila[2], int(fila[3]), fila[4], int(fila[5])))

    with open('libros.csv', mode='r', encoding='utf-8') as f:
        lector_csv = csv.reader(f)
        encabezados = next(lector_csv)
        for fila in lector_csv:
            grafo.agregar_aristas(Nodo(int(fila[0]), fila[1], fila[2], int(fila[3]), fila[4], int(fila[5])))

    return grafo

def comparar_peso(a):
    return a.peso


if __name__ == "__main__":
    personas = agregar_personas()
    grafo = crear_grafo()
    try:
        persona = input("Ingrese un nombre que se encuentre en la base de datos: ").lower()
    except:
        print("Ingrese un nombre valido")
    
    if persona not in [x.nombre_persona for x in personas]:
        print("Nombre no encontrado en la base de datos")
        exit()

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
        if i.origen.nombre == lended_book.nombre:
            recomendaciones.append(i)

    recomendaciones.sort(key=comparar_peso)
    recomendaciones.reverse()
    print()
    print("-"*60)
    print("Te podrian interesar los siguientes libros: ")
    print("-"*60)
    print()
    cont = 1
    for i in recomendaciones:
        print(f"{cont}. {i.destino}\n")
        cont +=1