import json
import os
from persistencia.log_manager import escribir_log

JSON_FILE = os.path.join("datos", "tareas.json")

def cargar_json():
    if not os.path.exists(JSON_FILE):
        escribir_log("JSON no existe, se crean estructuras vacías.")
        return [], [], []

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            datos = json.load(f)
        if not isinstance(datos, dict) or any(
            not isinstance(datos.get(clave), list)
            for clave in ("cola", "historial", "finalizadas")
        ):
            raise ValueError("El JSON no contiene las estructuras esperadas.")
        return datos["cola"], datos["historial"], datos["finalizadas"]
    except (OSError, json.JSONDecodeError, ValueError) as error:
        escribir_log(f"Error al cargar JSON: {error}")
        raise ValueError(
            f"No se pudieron cargar los datos de {JSON_FILE}; "
            "el archivo se conserva sin sobrescribir."
        ) from error

def guardar_json(cola, historial, finalizadas):
    os.makedirs(os.path.dirname(JSON_FILE), exist_ok=True)
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "cola": cola,
            "historial": historial,
            "finalizadas": finalizadas
        }, f, indent=4)
    escribir_log("Datos guardados en JSON.")
