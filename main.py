from servicios import *

def menu():
    while True:
        print("\n--- PhotoCampus ---")
        print("1. Agregar servicio")
        print("2. Listar servicios")
        print("3. Editar servicio")
        print("4. Eliminar servicio")
        print("5. Salir")

        op = input("Seleccione opción: ")

        if op == "1":
            agregar_servicio()
        elif op == "2":
            listar_servicios()
        elif op == "3":
            editar_servicio()
        elif op == "4":
            eliminar_servicio()
        elif op == "5":
            break
        else:
            print("Opción inválida")

menu()