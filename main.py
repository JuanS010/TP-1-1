import logica

def ciclo_del_juego():
    nivel = 1
    total_movs = 0
    movimientos = logica.asignar_movimientos(logica.GRILLA)
    juego = logica.empezar_nivel(nivel)
    print(f"NIVEL {nivel}")
    print()

    while True:

        if logica.juego_ganado(juego):
            if nivel == 5:
                print(f"Ganaste en un total de {total_movs} movimientos")
                print(f"Llegaste al nivel {nivel}")
                break
            else:
                nivel += 1
                print(f"Avanzaste al NIVEL {nivel}")
                print()
                movimientos = logica.asignar_movimientos(logica.GRILLA)
                juego = logica.empezar_nivel(nivel)

        if movimientos == 0:
            logica.mostrar_juego(juego)
            print(f"Perdiste. En total se usaron {total_movs} movimientos")
            print(f"Llegaste al nivel {nivel}")
            break  

        logica.mostrar_juego(juego)
        fila, columna = logica.pedir_instruccion()
        logica.generar_instruccion(juego, fila, columna)
        movimientos -= 1
        total_movs += 1

ciclo_del_juego()