#IMPORTANTE ACLARAR QUE CONSIDERO QUE MI LABERINTO ESTÁ AL REVÉS

laberinto = [
    ['camino', 'X', 'X', 'X', 'X'], 
    ['camino', 'X', 'camino', 'camino', 'camino'],
    ['camino', 'X', 'camino', 'X', 'camino'], 
    ['camino', 'camino', 'camino', 'X', 'camino'], 
    ['X', 'X', 'X', 'X', 'S']
    ]

x = 0
y = 0


print("Empiezas en la posición (0,0)")
print((laberinto[y])[x])
listarespuestas = ["","","","","","","","","","","","",""]
i = 0

while (laberinto[y])[x] == 'camino':
    direccion = input("Selecciona a la dirección a la cual quieres ir: ARRIBA, ABAJO, IZQUIERDA, DERECHA  >>>>  ")
    
    if direccion == "ABAJO" or "ARRIBA" or "IZQUIERDA" or "DERECHA":
        print("Has seleccionado {}".format(direccion))
        listarespuestas[i] = direccion
        i = i + 1
        
    if direccion == "ABAJO":
        x = x
        y = y - 1
    elif direccion == "ARRIBA":
        x = x
        y = y + 1
    elif direccion == "IZQUIERDA":
        x = x - 1
        y = y
    elif direccion == "DERECHA":
        x = x + 1
        y = y
    else:
        print("SOLO SE PUEDEN ELEGIR LAS OPCIONES DE DIRECCIÓN EXPLICADAS, ELIGE BIEN")
        print("\n")
    

    print("Estás en la casilla ({},{})".format(x,y))
    if (laberinto[y])[x] == 'camino':
        print("La casilla elegida NO es un muro, puede continuar en el laberinto")
    elif (laberinto[y])[x] == 'S':
        print("Has llegado a la salida del laberibnto. ¡HAS GANADO!")
        break
    else:
        print("La casilla es un muro \nReinicia el programa para seguir jugando")


print("LOS MOVIMIENTOS UTILIZADOS HAN SIDO:")
print(listarespuestas)