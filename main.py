from servicios import *

while True:

    print(
        "---PhotoCampus---\n"
        "1. Agregar Servicio\n"
        "2. Listar Servicio\n"
        "3. Editar Servicio\n"
        "4. Eliminar Servicio\n"
        "5. Salir"
    )

    opcion = int(input("Digite su opcion: "))

    match opcion:
        case 1:
            agregar_servicio()
        case 2:
            listar_servicios()
        case 3:
            editar_servicio()
        case 4: 
            eliminar_servicio()
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Error, opcion invalida")
