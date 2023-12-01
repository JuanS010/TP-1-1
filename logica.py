GRILLA = 5
INDICE_LETRA = ["A","B","C","D","E","F","G","H","i","j"]
LETRAS_POSIBLES = "AaBbCcDdEeFfGgHhIiJj"
FILA_VACIA = [-1,-1,-1,-1,-1]
NIVELES = [
    [[1,1,-1,1,1],[1,-1,1,-1,1],[-1,1,1,1,-1],[1,-1,1,-1,1],[1,1,-1,1,1]], # Nivel 1
    [[-1,1,-1,1,-1],[1,1,-1,1,1],[-1,1,-1,1,-1],[1,-1,1,-1,1],[1,-1,1,-1,1]], # Nivel 2
    [[1,-1,-1,-1,1],[1,1,-1,1,1],[-1,-1,1,-1,-1],[1,-1,1,-1,-1],[1,-1,1,1,-1]], # Nivel 3
    [[1,1,-1,1,1],[-1,-1,-1,-1,-1],[1,1,-1,1,1],[-1,-1,-1,-1,1],[1,1,-1,-1,-1]], # Nivel 4
    [[-1,-1,-1,1,1],[-1,-1,-1,1,1],[-1,-1,-1,-1,-1],[1,1,-1,-1,-1],[1,1,-1,-1,-1]] # Nivel 5
]

def asignar_movimientos(grilla):
    """Asigna los movimientos para el nivel"""
    return grilla*3

def empezar_nivel(lvl_actual):
    """Genera la matriz inicial de cada nivel"""

    for n in range(len(NIVELES)):
        if n+1 == lvl_actual:
            juego = NIVELES[n]

    matrix = []
    for i in range(len(juego)):
        matrix.append([])
    for i in range(len(juego)):
        matrix[i] = juego[i].copy()

    if GRILLA > 5:
        for k in range(5, GRILLA):
            matrix.append(FILA_VACIA.copy())
        for j in range(5, GRILLA):
            for i in range(GRILLA):
                matrix[i].append(-1)

    if GRILLA < 5:
        for k in range(5-GRILLA):
            matrix.remove(matrix[-1])
        for l in range(5-GRILLA):
            for i in range(GRILLA):
                for j in range(1):
                    matrix[i].remove(matrix[i][j-1])

    return matrix

def juego_ganado(matrix):
    """Define si el estado del juego es ganado"""
    for i in range(GRILLA):
        if max(matrix[i]) == 1:
            return False
    return True

def mostrar_juego(matrix):
    """Imprime el juego en pantalla"""
    for n in range(GRILLA+1):
        if n == 0:
            print("    ", end="")
        else:
            print(f'{n} ', end="")
    for i in range(GRILLA):
        print()
        for j in range(GRILLA):
            if j == 0:                    
                print(f"{INDICE_LETRA[i]} | ", end="")
            if matrix[i][j] == -1:
                print(f'{". "}', end="")
            else:
                print(f'{"o "}', end="")
    print()
    print()

def pedir_instruccion():
    """Pide la siguiente instruccion"""
    instruccion = input("Ingrese su jugada: ")
    if len(instruccion) != 2 or instruccion[0] not in LETRAS_POSIBLES or instruccion[1].isdecimal() == False :
        estado = False
        while estado == False:
            print()
            print("La jugada debe ser del tipo: 'A1'")
            instruccion = input("Ingrese su jugada: ")
            if len(instruccion) != 2 or instruccion[0] not in LETRAS_POSIBLES or instruccion[1].isdecimal() == False :
                continue
            break

    columna = int(instruccion[1])
    if instruccion[0] not in LETRAS_POSIBLES or not 1 <= columna <= GRILLA:
        print(f"La jugada debe ser en el rango A-{INDICE_LETRA[GRILLA-1]} 1-{GRILLA}")
        estadobis = False
        while estadobis == False:
            print()
            instruccion = input("Ingrese su jugada: ")
            if len(instruccion) != 2 or instruccion[0] not in LETRAS_POSIBLES or instruccion[1].isdecimal() == False :
                print("La jugada debe ser del tipo: 'A1'")
                continue
            columna = int(instruccion[1])
            if instruccion[0] not in LETRAS_POSIBLES or not 1 <= columna <= GRILLA :
                print(f"La jugada debe ser en el rango A-{INDICE_LETRA[GRILLA-1]} 1-{GRILLA}")
                continue
            break
            
    print()

    columna -= 1

    for i in range(0, len(LETRAS_POSIBLES), 2):
        if instruccion[0] in LETRAS_POSIBLES[i] or instruccion[0] in LETRAS_POSIBLES[i+1]:
            fila = int(i/2)
            break

    return fila, columna

def generar_instruccion(matrix, fila, columna):
    """Actualiza el juego con la nueva instruccion"""

    matrix[fila][columna] *= -1

    if fila != 0:
        matrix[fila-1][columna] *= -1
    if fila != (GRILLA-1):
        matrix[fila+1][columna] *= -1
    
    if columna != 0:
        matrix[fila][columna-1] *= -1
    if columna != (GRILLA-1):
        matrix[fila][columna+1] *= -1

    return matrix