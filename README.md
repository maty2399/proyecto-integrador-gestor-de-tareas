# Nombre del Proyecto: Gestor de Tareas Colaborativo

## Integrantes
* Gabriela Nieva
* Belen Mancilla 
* Daniela Pulin
* Villegas Matías

---

## Descripción Breve
Aplicación de consola desarrollada en Python bajo el paradigma de programación estructurada. Permite gestionar un sistema de tareas colaborativo con prioridades, estados y fechas límite. Incluye persistencia de datos en archivos JSON y CSV, registro de logs en TXT, control de excepciones, validaciones estrictas de entradas y funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.
A modo de investigación, se incursionará en dar una salida visual front end.

---

## Instrucciones de Instalación y Ejecución

1. Crear una carpeta vacía en el equipo, abrir la consola (Git Bash Here) y ejecutar:
   ```bash
   git clone [https://github.com/maty2399/proyecto-integrador-gestor-de-tareas.git](https://github.com/maty2399/proyecto-integrador-gestor-de-tareas.git)

2. Ingresar a la carpeta del proyecto y abrir el editor con:
   
   code .

3. Organización y asignación de tareas (Metodología de equipo)

   * El equipo coordinó la distribución de roles y subtareas a través de reuniones en Discord.

   * Se centralizó la planificación, el seguimiento de pendientes y el estado de avance utilizando un tablero compartido en Trello (separando en columnas como Tareas a realizar, En proceso y Finalizado).

4. Control de versiones mediante ramas de trabajo
   Antes de modificar o crear un módulo, cada integrante crea y se posiciona en una rama específica desde la terminal de Visual Studio Code:

   git checkout -b feature/<nombre-de-la-tarea>

   (Es una buena práctica obligatoria en desarrollo de software. Evita romper la rama principal (main) y permite que cada integrante trabaje en su funcionalidad de forma aislada antes de fusionar los cambios.)

5. Ejecución de la aplicación

   * Ejecutar el script principal de orquestación del menú desde la terminal:
   
     - python main.py

6. Estructura de Archivos del Proyecto

   El código se encuentra modularizado separando responsabilidades:

   * main.py: Punto de entrada, menú principal y orquestación de flujos.

   * estructuras.py: Definición de constructores y estructuras de datos (listas de diccionarios).

   * persistencia.py: Lógica de lectura y escritura de archivos (JSON, CSV y logs en TXT).

   * utils.py: Funciones auxiliares de validación, búsqueda y ordenamiento.

   * estadisticas.py: Cálculo de métricas y reportes del sistema.

7. Bibliotecas Utilizadas

   * json: Serialización y deserialización de datos estructurados.

   * csv: Exportación de reportes tabulares.

   * datetime: Registro de marcas de tiempo (timestamps) para el log de operaciones.

   * os: Verificación y control de existencia de archivos en el sistema local.

8. Créditos de Uso de IA

   En cumplimiento con las directrices de la cátedra sobre el uso responsable de inteligencia artificial, se emplearon herramientas de asistencia (ChatGPT/Gemini) como apoyo en el diseño lógico de funciones, consultas de depuración de errores en bloques try/except y verificación del estándar de nomenclatura snake_case. Todo el código fue analizado, adaptado y documentado por el equipo.