# Hundir la Flota en Python

Este proyecto es una implementación del clásico juego "Hundir la Flota" usando Python. El objetivo es hundir todos los barcos del oponente antes de que él hunda los tuyos. ¡Prepárate para la batalla naval! 

---

## **Características del Juego**
- **Tablero de 10x10:** Cada jugador tiene un tablero de 10 filas por 10 columnas.
- **Barcos Aleatorios:** Los barcos se colocan aleatoriamente en el tablero sin superposición.
  - **Esloras de barcos:**
    - 3 barcos de 2 casillas.
    - 2 barcos de 3 casillas.
    - 1 barco de 4 casillas.
- **Mecánica de Disparo:**
  - **X:** Barco tocado.
  - **A:** Agua.
- **Turnos Alternos:** El jugador y el PC disparan por turnos.
- **Victoria:** El primero en hundir todos los barcos del oponente gana.

---

## **Competencias Utilizadas**
Este proyecto fue desarrollado utilizando las siguientes habilidades y conocimientos de programación:

- **Estructuras de datos:**
  - Uso de listas para representar el tablero.
  - Almacenamiento de las coordenadas de los barcos como listas de tuplas.
- **Control de flujo:**
  - Condicionales (`if`, `else`) para verificar los disparos y resultados.
  - Bucles (`for`, `while`) para iterar sobre el tablero y gestionar turnos.
- **Funciones:**
  - Definición de funciones modulares para facilitar la organización del código (`crear_tablero`, `crear_barco`, `disparar`, etc.).
  - Uso de parámetros y valores de retorno para comunicación entre funciones.
- **Manejo de errores:**
  - Captura de entradas inválidas con `try` y `except`.
- **Programación aleatoria:**
  - Uso de la biblioteca `random` para la colocación de barcos y disparos del PC.
- **Validación de datos:**
  - Verificación de coordenadas válidas en el tablero.
  - Prevención de disparos repetidos.
- **Diseño lógico:**
  - Gestión del estado del juego (turnos, barcos hundidos, condiciones de victoria).
  - Separación del tablero del usuario y del PC para mantener la integridad del juego.
- **Comunicación y visualización:**
  - Impresión legible de los tableros con información relevante para cada turno.
  - Mensajes claros para el usuario sobre los resultados de cada disparo.
