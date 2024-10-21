postres = []

def agregar_postre(nombre, ingredientes):
    for postre in postres:
        if postre[0] == nombre:
            print(f"El postre '{nombre}' ya existe.")
            return
    postres.append([nombre, ingredientes])
    print(f"Postre '{nombre}' agregado con ingredientes: {', '.join(ingredientes)}.")

def eliminar_postre(nombre):
    for postre in postres:
        if postre[0] == nombre:
            print(f"Ingredientes de '{nombre}': {', '.join(postre[1])}")
            postres.remove(postre)
            print(f"Postre '{nombre}' eliminado, pero los ingredientes han sido conservados.")
            return
    print(f"El postre '{nombre}' no existe.")

def mostrar_ingredientes_postre(nombre):
    for postre in postres:
        if postre[0] == nombre:
            if postre[1]:
                print(f"Ingredientes de '{nombre}': {', '.join(postre[1])}")
            else:
                print(f"No hay ingredientes para '{nombre}'.")
            return
    print(f"El postre '{nombre}' no existe.")

def mostrar_todos_postres():
    if postres:
        print("\nLista de postres y sus ingredientes:")
        for postre in postres:
            print(f"Postre: {postre[0]}, Ingredientes: {', '.join(postre[1])}")
    else:
        print("No hay postres registrados.")

def agregar_ingrediente_postre(nombre, ingrediente):
    for postre in postres:
        if postre[0] == nombre:
            if ingrediente not in postre[1]:
                postre[1].append(ingrediente)
                print(f"Ingrediente '{ingrediente}' agregado a '{nombre}'.")
            else:
                print(f"El ingrediente '{ingrediente}' ya está en '{nombre}'.")
            return
    print(f"El postre '{nombre}' no existe.")

def eliminar_ingredientes_postre(nombre):
    for postre in postres:
        if postre[0] == nombre:
            postre[1].clear()
            print(f"Todos los ingredientes de '{nombre}' han sido eliminados.")
            return
    print(f"El postre '{nombre}' no existe.")

def eliminar_postres_repetidos():
    global postres
    postres_unicos = []
    nombres_vistos = set()
    
    for postre in postres:
        nombre = postre[0]
        if nombre not in nombres_vistos:
            nombres_vistos.add(nombre)
            postres_unicos.append(postre)
        else:
            print(f"El postre '{nombre}' ya estaba registrado y se eliminó.")
    
    postres = postres_unicos

def main():
    while True:
        print("\n Menú de la Gestión de los Postres ")
        print("1. Agregar el postre")
        print("2. Eliminar el postre (conservar ingredientes)")
        print("3. Mostrar ingredientes de un postre")
        print("4. Agregar ingrediente a un postre en específico")
        print("5. Eliminar todos los ingredientes de un postre en específico")
        print("6. Mostrar todos los postres")
        print("7. Eliminar postres repetidos")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_postre = input("Ingrese el nombre del postre: ")
            ingredientes = input("Ingrese los ingredientes separados por comas: ").split(',')
            ingredientes = [ingrediente.strip() for ingrediente in ingredientes]
            agregar_postre(nombre_postre, ingredientes)

        elif opcion == "2":
            nombre_postre = input("Ingrese el nombre del postre a eliminar: ")
            eliminar_postre(nombre_postre)

        elif opcion == "3":
            nombre_postre = input("Ingrese el nombre del postre: ")
            mostrar_ingredientes_postre(nombre_postre)

        elif opcion == "4":
            nombre_postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a agregar: ")
            agregar_ingrediente_postre(nombre_postre, ingrediente)

        elif opcion == "5":
            nombre_postre = input("Ingrese el nombre del postre: ")
            eliminar_ingredientes_postre(nombre_postre)

        elif opcion == "6":
            mostrar_todos_postres()

        elif opcion == "7":
            eliminar_postres_repetidos()

        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
