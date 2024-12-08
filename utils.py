import random

def crear_tablero():
    tamaño = 10
    tablero = []
    for _ in range(tamaño):
        fila = ["_"] * tamaño
        tablero.append(fila)
    return tablero

def crear_barco(eslora, tamaño):
    direccion = random.choice(["horizontal", "vertical"])
    if direccion == "horizontal":
        fila = random.randint(0, tamaño - 1)
        columna_inicio = random.randint(0, tamaño - eslora)
        coordenadas = [(fila, columna_inicio + i) for i in range(eslora)]
    else:
        columna = random.randint(0, tamaño - 1)
        fila_inicio = random.randint(0, tamaño - eslora)
        coordenadas = [(fila_inicio + i, columna) for i in range(eslora)]
    return direccion, coordenadas

def colocar_barco_en_tablero(tablero):
    barcos_eslora = [2, 2, 2, 3, 3, 4]
    lista_barcos = []
    for eslora in barcos_eslora:
        while True:
            direccion, barco = crear_barco(eslora, len(tablero))
            if all(tablero[fila][columna] == "_" for fila, columna in barco):
                for fila, columna in barco:
                    tablero[fila][columna] = "O"
                lista_barcos.append((direccion, barco))
                break
    return lista_barcos

def mostrar_tablero_usuario(tablero):
    print("\nTablero del Usuario:")
    for fila in tablero:
        print(" ".join(fila))

def mostrar_tablero_pc(tablero):
    print("\nTablero del PC:")
    for fila in tablero:
        print(" ".join("X" if casilla == "X" else "A" if casilla == "A" else "_" for casilla in fila))

def disparar(casilla, tablero, barcos):
    fila, columna = casilla
    barcos_hundidos=[]
    if tablero[fila][columna] == "O":
        print(f"Disparo en {casilla}: ¡Tocado!")
        tablero[fila][columna] = "X" 
        
        for direccion, barco in barcos:
            if all(tablero[fila][columna] == "X" for fila, columna in barco):
                print(f"¡Barco hundido! Coordenadas: {barco}")
                barcos_hundidos.append(barco)
                
    elif tablero[fila][columna] == "_":
        print(f"Disparo en {casilla}: ¡Agua!")
        tablero[fila][columna] = "A"
    else:
        print(f"Disparo en {casilla}: Ya disparaste aquí.")


def todos_hundidos(tablero):
    return not any("O" in fila for fila in tablero)

def turnos(tablero_usuario, tablero_pc, barcos_usuario, barcos_pc):
    turno = "usuario" 
    while True:
        if turno == "usuario": 
            print("\nTu turno:")
            mostrar_tablero_usuario(tablero_usuario)
            mostrar_tablero_pc(tablero_pc)
            while True:
                try:
                    fila = int(input("Introduce la fila del disparo (0-9): "))
                    if 0<=fila<=9:
                        break
                    else:
                        print("Por favor. Introduce un número entre el 0 y el 9")
                except ValueError:
                    print("Entrada no válida. Introduce un número válido")
                
            while True:
                try:
                    columna = int(input("Introduce la columna del disparo (0-9): "))
                    if 0<=columna<=9:
                        break
                    else:
                        print("Por favor. Introduce un número entre el 0 y el 9")
                except ValueError:
                    print("Entrada no válida. Introduce un número válido")

            disparar((fila, columna), tablero_pc, barcos_pc)
            if todos_hundidos(tablero_pc):
                print("¡Felicidades! Hundiste todos los barcos del PC. ¡Ganaste!")
                break
            if tablero_pc[fila][columna] != "X":
                turno = "pc"
        else:
            print("\nTurno del PC:")
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            print(f"El PC dispara en ({fila}, {columna})")
            disparar((fila, columna), tablero_usuario, barcos_usuario)
            mostrar_tablero_usuario(tablero_usuario)
            if todos_hundidos(tablero_usuario):
                print("¡Lo siento! El PC hundió todos tus barcos. ¡Perdiste!")
                break
            if tablero_usuario[fila][columna] != "X":
                turno = "usuario"


tablero_usuario = crear_tablero()
tablero_pc = crear_tablero()
barcos_usuario = colocar_barco_en_tablero(tablero_usuario)
barcos_pc = colocar_barco_en_tablero(tablero_pc)
turnos(tablero_usuario, tablero_pc, barcos_usuario, barcos_pc)