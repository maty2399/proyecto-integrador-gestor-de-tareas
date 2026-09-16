from datetime import datetime
import os

LOG_FILE = os.path.join("datos", "log.txt")

def escribir_log(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha}] {mensaje}\n"

    # Crear carpeta datos si no existe
    if not os.path.exists("datos"):
        os.makedirs("datos")

    # Escribir el log
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(linea)
    except IOError:
        print("No se pudo escribir en el archivo de log.")
