# PhotoCampus_Raymond_Frayden_JuanMa_Yojhan.
PhotoCampus es un sistema desarrollado en Python que permite gestionar servicios fotográficos como bodas, retratos y fotografía de productos.

El sistema permite registrar información como el nombre del servicio, precio, tipo de evento y duración estimada, facilitando la organización y administración de los servicios ofrecidos.

El proyecto fue desarrollado en Visual Studio Code y utilizando Git para el control de versiones.

Ejercicios hechos en Visual Studio Code.


Requisitos:
Python 3 instalado.
Git instalado.
Editor de código (Visual Studio Code recomendado).

Sistema para gestionar servicios fotográficos como bodas, retratos y productos.

1. Clonar el repositorio.
2. Ejecutar:
   main.py.

- main.py → programa principal.
- servicios.py → lógica del negocio.
- almacenamiento.py → manejo de JSON.
- servicios.json → base de datos.


El sistema permite:

Agregar servicios fotográficos.
Listar servicios registrados.
Editar servicios existentes.
Eliminar servicios.

Los datos se almacenan en el archivo servicios.json, lo que permite conservar la información incluso después de cerrar el programa.

Estructura del repositorio.
main.py → Programa principal.
servicios.py → Lógica del negocio (operaciones CRUD).
almacenamiento.py → Manejo de lectura y escritura del archivo JSON.
servicios.json → Archivo de almacenamiento de datos.

Se usaron ramas:
- feature/add-services.
- feature/edit-services.
- feature/delete-services.


Cada funcionalidad fue desarrollada de forma independiente y posteriormente integrada a la rama principal mediante procesos de merge.

Se generó un conflicto al modificar la misma línea en diferentes ramas.
Fue resuelto manualmente editando el archivo afectado.

Yojhan Andres Vega Miranda.
Juan Manuel Gouveia Ortiz
Frayden Stiven Garcia Urbina.
Raymond Javier Zabala Sanchez.