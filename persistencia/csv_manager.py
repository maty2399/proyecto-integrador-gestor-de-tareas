import csv
import os
from persistencia.log_manager import escribir_log

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FILE = os.path.join(PROJECT_DIR, "datos", "reporte.csv")

def exportar_csv(lista):
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["Identificador", "Título", "Prioridad", "Estado",
                    "Fecha límite", "Categoría", "Responsable",
                    "Creación", "Finalización"])
        for t in lista:
            w.writerow(t)

    escribir_log("CSV exportado correctamente.")
    return CSV_FILE
