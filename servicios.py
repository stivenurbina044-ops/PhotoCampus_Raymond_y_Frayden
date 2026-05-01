from almacenamiento import cargar_servicios, guardar_servicios

def agregar_servicio():
    servicios = cargar_servicios()
    
    nombre = input("Nombre del servicio: ")
    precio = float(input("Precio: "))
    tipo = input("Tipo de evento: ")
    duracion = int(input("Duración (horas): "))

    nuevo = {
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo,
        "duracion": duracion
    }

    servicios.append(nuevo)
    guardar_servicios(servicios)
    print("Servicio agregado correctamente")

def listar_servicios():
    servicios = cargar_servicios()
    for i, s in enumerate(servicios):
        print(f"{i}. {s}")

def editar_servicio():
    servicios = cargar_servicios()
    listar_servicios()

    i = int(input("Seleccione índice a editar: "))
    servicios[i]["nombre"] = input("Nuevo nombre: ")
    servicios[i]["precio"] = float(input("Nuevo precio: "))

    guardar_servicios(servicios)
    print("Servicio actualizado")

def eliminar_servicio():
    servicios = cargar_servicios()
    listar_servicios()

    i = int(input("Seleccione índice a eliminar: "))
    servicios.pop(i)

    guardar_servicios(servicios)
    print("Servicio eliminado")