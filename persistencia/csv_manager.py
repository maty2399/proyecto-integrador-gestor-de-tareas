import csv
import os
from persistencia.log_manager import escribir_log

CSV_FILE = os.path.join("datos", "reporte.csv")

def exportar_csv(lista):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Título", "Prioridad", "Estado",
                    "Fecha límite", "Categoría", "Responsable",
                    "Creación", "Finalización"])
        for t in lista:
            w.writerow(t)

    escribir_log("CSV exportado correctamente.")
