# Registro de Uso de Inteligencia Artificial (PROMPTS.md)

Este documento detalla el uso responsable de herramientas de Inteligencia Artificial (ChatGPT / Gemini) como soporte técnico, de consulta y de buenas prácticas durante el desarrollo del Proyecto Integrador del Gestor de Tareas Colaborativo.

---

## 1. Metodológia de Uso
Las herramientas de IA se emplearon exclusivamente bajo los siguientes criterios:
* Asistencia conceptual y de sintaxis: Consultas sobre manejo de estructuras de datos en Python, sintaxis de bloques `try/except` y     diseño modular.
* Depuración de errores : Análisis de mensajes de error en terminal para corregir excepciones no controladas.
* Buenas prácticas:** Verificación del cumplimiento del estándar de nomenclatura en `snake_case` y estructuración de documentación (`README.md`).

---

## 2. Bitácora de Consultas Clave (Prompts y Respuestas de Referencia)

### Consulta 1: Estructuración y formato del archivo README.md
* Prompt del usuario:** 
  > *"¿Cómo puedo estructurar el archivo README.md de un proyecto integrador en Python para que incluya instrucciones de instalación, organización del equipo con Trello/Discord, estructura de archivos y créditos de uso de IA?"*

* **Respuesta / Asistencia de la IA:** 
  Se proporcionó una plantilla en formato Markdown estructurada por secciones claras (`#`, `##`), bloques de código delimitados para comandos de terminal (`bash`), y viñetas descriptivas para detallar el rol de cada módulo (`main.py`, `persistencia.py`, etc.).

### Consulta 2: Manejo de excepciones y control de entradas numéricas
* **Prompt del usuario:** 
  > *"¿Cómo puedo evitar que mi menú en Python rompa si el usuario ingresa una letra en lugar de un número?"*
* **Respuesta / Asistencia de la IA:** 
  Se sugirió el uso de una estructura de control basada en bloques `try-except` combinados con un bucle `while`:
  ```python
  while True:
      try:
          opcion = int(input("Ingrese una opción: "))
          break
      except ValueError:
          print("Error: Debe ingresar un número entero válido.")

Consulta: Buenas prácticas de control de versiones con Git

Prompt:

"¿Cuáles son los comandos correctos para crear una rama de trabajo, hacer commit de un archivo específico y pushearla a GitHub sin afectar la rama main?"

Respuesta / Asistencia de la IA:
Se detalló la secuencia de comandos de Git:

git checkout -b feature/<nombre-tarea>

git add <archivo>

git commit -m "mensaje"

git push -u origin <nombre-rama>

3. Declaración de Autoría

* **Todo el código fuente, la lógica de programación y las decisiones de diseño implementadas en el sistema fueron analizadas, probadas y adaptadas por el equipo de desarrollo. La IA funcionó estrictamente como una herramienta de consulta y apoyo pedagógico.**