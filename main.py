from datetime import datetime

from persistencia.log_manager import escribir_log
from persistencia.json_manager import cargar_json, guardar_json
from persistencia.csv_manager import exportar_csv
from estructuras.cola import agregar_tarea, eliminar_tarea, listar_cola
from estructuras.finalizadas import agregar_finalizada, listar_finalizadas
from estructuras.historial import agregar_historial, obtener_historial

def generar_id(cola, finalizadas):
    ids = [t[0] for t in cola] + [t[0] for t in finalizadas]
    return max(ids) + 1 if ids else 1


def alta_tarea(cola, historial):
    print("\n--- Alta de tarea ---")
    titulo = input("Título: ")
    prioridad = input("Prioridad: ")
    fecha_limite = input("Fecha límite (DD-MM-YYYY): ")
    categoria = input("Categoría: ")
    responsable = input("Responsable: ")

    id_nuevo = generar_id(cola, [])
    fecha_creacion = datetime.now().strftime("%d%m%Y %H:%M:%S")

    tarea = [
        id_nuevo, titulo, prioridad, "pendiente",
        fecha_limite, categoria, responsable,
        fecha_creacion, None
    ]

    agregar_tarea(cola, tarea)
    agregar_historial(historial, id_nuevo, "pendiente", fecha_creacion)
    escribir_log(f"Tarea creada ID {id_nuevo}")


def cambiar_estado(cola, historial, finalizadas):
    print("\n--- Cambiar estado ---")
    id_buscar = int(input("ID de tarea: "))

    tarea = next((t for t in cola if t[0] == id_buscar), None)
    if tarea is None:
        print("No existe la tarea.")
        return

    nuevo_estado = input("Nuevo estado: ").lower()
    fecha = datetime.now().strftime("%d%m%Y--%H:%M:%S")

    tarea[3] = nuevo_estado
    agregar_historial(historial, id_buscar, nuevo_estado, fecha)

    if nuevo_estado == "finalizada":
        tarea[8] = fecha
        agregar_finalizada(finalizadas, tarea)
        eliminar_tarea(cola, tarea)

    escribir_log(f"Estado cambiado ID {id_buscar}")


def menu():
    cola, historial, finalizadas = cargar_json()

    while True:
        print("\n===== Gestor de tareas =====")
        print("1. Alta de tarea")
        print("2. Cambiar estado")
        print("3. Listar tareas")
        print("4. Exportar CSV")
        print("5. Salir")

        op = input("Opción: ")

        if op == "1":
            alta_tarea(cola, historial)
        elif op == "2":
            cambiar_estado(cola, historial, finalizadas)
        elif op == "3":
            print(listar_cola(cola))
            print(listar_finalizadas(finalizadas))
            print(obtener_historial(historial))
        elif op == "4":
            exportar_csv(cola + finalizadas)
        elif op == "5":
            guardar_json(cola, historial, finalizadas)
            escribir_log("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
