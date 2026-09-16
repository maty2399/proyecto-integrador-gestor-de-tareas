import json
import csv
import os
from datetime import datetime

JSON_FILE = "tareas.json"
CSV_FILE = "reporte.csv"
LOG_FILE = "log.txt"


# ------------------ LOG ------------------

def escribir_log(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha}] {mensaje}\n"
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(linea)
    except:
        print("Advertencia: no se pudo escribir en el log.")


# ------------------ PERSISTENCIA ------------------

def cargar_datos():
    if not os.path.exists(JSON_FILE):
        escribir_log("JSON no existe, se crean estructuras vacías.")
        return [], [], []

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            datos = json.load(f)
            escribir_log("Datos cargados desde JSON.")
            return datos["cola"], datos["historial"], datos["finalizadas"]
    except:
        escribir_log("Error al cargar JSON, se crean estructuras vacías.")
        return [], [], []


def guardar_datos(cola, historial, finalizadas):
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "cola": cola,
                "historial": historial,
                "finalizadas": finalizadas
            }, f, indent=4)
        escribir_log("Datos guardados en JSON.")
    except:
        escribir_log("Error al guardar JSON.")


# ------------------ GENERAR ID ------------------

def generar_id(cola, finalizadas):
    ids = []
    for t in cola:
        ids.append(t[0])
    for t in finalizadas:
        ids.append(t[0])
    if not ids:
        return 1
    return max(ids) + 1


# ------------------ ALTA DE TAREA ------------------

def alta_tarea(cola, historial):
    print("\n--- Alta de tarea ---")
    titulo = input("Título: ")
    prioridad = input("Prioridad (alta/media/baja): ").lower()
    fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
    categoria = input("Categoría: ")
    responsable = input("Responsable: ")

    id_nuevo = generar_id(cola, [])
    fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tarea = [
        id_nuevo, titulo, prioridad, "pendiente",
        fecha_limite, categoria, responsable,
        fecha_creacion, None
    ]

    cola.append(tarea)

    historial.append([id_nuevo, "pendiente", fecha_creacion])

    escribir_log(f"Alta tarea ID {id_nuevo} - {titulo}")
    print("Tarea creada.")


# ------------------ CAMBIO DE ESTADO ------------------

def cambiar_estado(cola, historial, finalizadas):
    print("\n--- Cambiar estado ---")
    try:
        id_buscar = int(input("ID de tarea: "))
    except:
        print("ID inválido.")
        return

    tarea = None
    for t in cola:
        if t[0] == id_buscar:
            tarea = t
            break

    if tarea is None:
        print("No existe la tarea.")
        return

    print(f"Estado actual: {tarea[3]}")
    nuevo_estado = input("Nuevo estado (pendiente/en curso/finalizada): ").lower()

    if nuevo_estado not in ["pendiente", "en curso", "finalizada"]:
        print("Estado inválido.")
        return

    tarea[3] = nuevo_estado
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    historial.append([id_buscar, nuevo_estado, fecha])

    if nuevo_estado == "finalizada":
        tarea[8] = fecha
        finalizadas.append(tarea)
        cola.remove(tarea)

    escribir_log(f"Cambio estado tarea {id_buscar} → {nuevo_estado}")
    print("Estado actualizado.")


# ------------------ LISTAR ------------------

def mostrar_tarea(t):
    print(f"ID {t[0]} | {t[1]} | Prioridad: {t[2]} | Estado: {t[3]} | Responsable: {t[6]} | Límite: {t[4]}")


def listar_tareas(cola, finalizadas):
    print("\n--- Tareas activas ---")
    if not cola:
        print("No hay tareas activas.")
    else:
        for t in cola:
            mostrar_tarea(t)

    print("\n--- Tareas finalizadas ---")
    if not finalizadas:
        print("No hay finalizadas.")
    else:
        for t in finalizadas:
            mostrar_tarea(t)


# ------------------ FILTROS ------------------

def filtrar_tareas(cola, finalizadas):
    print("\n--- Filtros ---")
    print("1. Por estado")
    print("2. Por categoría")
    print("3. Por responsable")
    op = input("Opción: ")

    todas = cola + finalizadas
    resultado = []

    if op == "1":
        estado = input("Estado: ").lower()
        for t in todas:
            if t[3] == estado:
                resultado.append(t)

    elif op == "2":
        cat = input("Categoría: ").lower()
        for t in todas:
            if t[5].lower() == cat:
                resultado.append(t)

    elif op == "3":
        resp = input("Responsable: ").lower()
        for t in todas:
            if t[6].lower() == resp:
                resultado.append(t)

    else:
        print("Opción inválida.")
        return

    print("\n--- Resultado ---")
    if not resultado:
        print("No hay coincidencias.")
        return

    for t in resultado:
        mostrar_tarea(t)

    exp = input("¿Exportar a CSV? (s/n): ").lower()
    if exp == "s":
        exportar_csv(resultado)


# ------------------ ESTADÍSTICAS ------------------

def estadisticas(cola, finalizadas):
    print("\n--- Estadísticas ---")

    total = len(cola) + len(finalizadas)
    print(f"Total tareas: {total}")
    print(f"Activas: {len(cola)}")
    print(f"Finalizadas: {len(finalizadas)}")

    dias = []
    for t in finalizadas:
        try:
            f1 = datetime.strptime(t[7], "%Y-%m-%d %H:%M:%S")
            f2 = datetime.strptime(t[8], "%Y-%m-%d %H:%M:%S")
            delta = f2 - f1
            dias.append(delta.days)
        except:
            pass

    if dias:
        prom = sum(dias) / len(dias)
        print(f"Promedio días resolución: {prom:.2f}")
    else:
        print("No hay datos suficientes.")

    exp = input("¿Exportar estadísticas a CSV? (s/n): ").lower()
    if exp == "s":
        exportar_csv(finalizadas)


# ------------------ EXPORTAR CSV ------------------

def exportar_csv(lista):
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["ID", "Título", "Prioridad", "Estado",
                        "Fecha límite", "Categoría", "Responsable",
                        "Creación", "Finalización"])
            for t in lista:
                w.writerow(t)
        escribir_log("Exportación CSV realizada.")
        print("CSV generado.")
    except:
        escribir_log("Error al exportar CSV.")
        print("Error al generar CSV.")


# ------------------ MENÚ ------------------

def menu():
    cola, historial, finalizadas = cargar_datos()

    while True:
        print("\n===== Gestor de tareas (primitivo) =====")
        print("1. Alta de tarea")
        print("2. Cambiar estado")
        print("3. Listar tareas")
        print("4. Filtrar tareas")
        print("5. Estadísticas")
        print("6. Salir")

        op = input("Opción: ")

        if op == "1":
            alta_tarea(cola, historial)
        elif op == "2":
            cambiar_estado(cola, historial, finalizadas)
        elif op == "3":
            listar_tareas(cola, finalizadas)
        elif op == "4":
            filtrar_tareas(cola, finalizadas)
        elif op == "5":
            estadisticas(cola, finalizadas)
        elif op == "6":
            guardar_datos(cola, historial, finalizadas)
            escribir_log("Programa finalizado.")
            print("Adiós.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
