def mostrar_estadisticas(cola, finalizadas):
    """
    Calcula y muestra estadísticas de productividad basadas en los índices reales:
    [ID, Título, Prioridad, Estado, Fecha límite, Categoría, Responsable, Creación, Finalización]
    """
    # Combinamos la cola activa y las finalizadas para tener el universo total de tareas
    todas_las_tareas = cola + finalizadas
    total_general = len(todas_las_tareas)

    if total_general == 0:
        print("\nNo hay tareas registradas para calcular estadísticas.")
        return

    # 1. Conteo por estado (Índice 3)
    pendientes = sum(1 for t in todas_las_tareas if t[3] == "pendiente")
    en_curso = sum(1 for t in todas_las_tareas if t[3] == "en curso")
    total_finalizadas = len(finalizadas)

    # Porcentaje de cumplimiento
    porcentaje = (total_finalizadas / total_general) * 100

    # 2. Ranking de responsables (Índice 6)
    conteo_responsables = {}
    for tarea in todas_las_tareas:
        responsable = tarea[6] if tarea[6] else "Sin asignar"
        conteo_responsables[responsable] = conteo_responsables.get(responsable, 0) + 1

    # Impresión de resultados en consola
    print("\n" + "="*40)
    print("       ESTADÍSTICAS DE PRODUCTIVIDAD")
    print("="*40)
    print(f"Total de tareas en el sistema: {total_general}")
    print(f"  • Pendientes : {pendientes}")
    print(f"  • En curso   : {en_curso}")
    print(f"  • Finalizadas: {total_finalizadas}")
    print(f"Porcentaje de avance global: {porcentaje:.1f}%")
    
    print("\n--- Ranking de Responsables ---")
    for resp, cantidad in sorted(conteo_responsables.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {resp}: {cantidad} tarea(s) asignada(s)")
    print("="*40)