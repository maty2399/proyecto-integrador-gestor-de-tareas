# Registro de Uso de Inteligencia Artificial (PROMPTS.md)

Este documento detalla el uso responsable de herramientas de Inteligencia Artificial (ChatGPT / Gemini) como soporte técnico, de consulta y de buenas prácticas durante el desarrollo del Proyecto Integrador del Gestor de Tareas Colaborativo.

---

## 1. Lineamientos de Uso
Las herramientas de IA se emplearon exclusivamente bajo los siguientes criterios:
* **Asistencia conceptual y de arquitectura:** Consultas sobre modularización del código y separación de responsabilidades.
* **Depuración de errores (Debugging) y Code Review:** Análisis de código del Scrum Master para detectar posibles pérdidas de datos en archivos JSON y control de excepciones (`ValueError`).
* **Buenas prácticas:** Verificación del estándar de nomenclatura en `snake_case` y estructuración de documentación (`README.md`).

---

## 2. Bitácora de Consultas y Aportes del Equipo

### Arquitectura y Modularización
* **Consulta:** 
  > *"¿Cómo puedo organizar mi codigo para que se vea separado, de forma ordenada y facil de comprender?"*
* **Respuesta / Sugerencia de la IA:** 
  Se sugirió separar el desarrollo en módulos, carpetas y archivos independientes (`main.py`, `persistencia.py`, `utils.py`, etc.) para que el código quede limpio, modular y fácil de mantener.

### Scrum Master - Code Review y Detección de Riesgos
* **Consulta:** 
  > *"El flujo básico está armado pero ¿podrías considerar una asistencia y decirme si los datos están bien con sus respectivos niveles?"*
* **Respuesta / Hallazgos de la IA:** 
  Se realizó una revisión del código detectando dos áreas críticas a corregir para el Hito:
  1. **Nivel Alto (Persistencia):** Posible pérdida de datos si el archivo JSON se lee mal o está corrupto, ocultando el error y devolviendo datos vacíos que podrían sobrescribir el archivo original (`json_manager.py`).
  2. **Nivel Medio (Validaciones):** Riesgo de `ValueError` en el `main.py` al ingresar letras en lugar de identificadores numéricos, y necesidad de restringir los estados de las tareas a los valores permitidos (*pendiente*, *en curso*, *finalizada*).

### Consultas técnicas generales del equipo
* **Control de excepciones en menús:** Uso de bloques `try-except` combinados con bucles `while` para evitar caídas de la aplicación ante ingresos incorrectos del usuario.
* **Control de versiones con Git:** Uso de comandos para la gestión de ramas de características (*feature branches*) y control de fusiones.

---

## 3. Próximas Etapas
* **Desarrollo y correcciones:** Aplicar las correcciones sugeridas en el code review sobre persistencia y validaciones.
* **Front-end:** Integración de la capa visual a cargo de Belen hacia la etapa final del proyecto.

---

## 4. Declaración de Autoría
Todo el código fuente, la lógica de programación y las decisiones de diseño implementadas en el sistema fueron analizadas, probadas y adaptadas por el equipo de desarrollo. La IA funcionó estrictamente como una herramienta de consulta y apoyo pedagógico.