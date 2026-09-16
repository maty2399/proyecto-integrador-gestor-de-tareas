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
            return datos["cola"], datos["historial"], datos["finalizadas"]
    except:
        escribir_log("Error al cargar JSON.")
        return [], [], []

def guardar_json(cola, historial, finalizadas):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "cola": cola,
            "historial": historial,
            "finalizadas": finalizadas
        }, f, indent=4)
    escribir_log("Datos guardados en JSON.")
