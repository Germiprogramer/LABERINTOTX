laberinto = [
    ['camino', 'X', 'X', 'X', 'X'], 
    ['camino', 'X', 'A', 'camino', 'camino'],
    ['camino', 'X', 'camino', 'X', 'camino'], 
    ['camino', 'camino', 'camino', 'X', 'camino'], 
    ['X', 'X', 'X', 'X', 'S']
    ]

x = 0
y = 0


print("Empiezas en la posición (0,0)")
print((laberinto[y])[x])

while (laberinto[y])[x] == 'camino':
    direccion = input("Selecciona a la dirección a la cual quieres ir: ARRIBA, ABAJO, IZQUIERDA, DERECHA  >>>>  ")
    
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
        x = x
        y = y + 1
    else:
        print("elige bien")
    
    print((laberinto[y])[x])

    print("Estás en la casilla ({},{})".format(x,y))
    if (laberinto[y])[x] == 'camino':
        print("La casilla elegida NO es un muro, puede continuar en el laberinto")
    else:
        print("La casilla es un muro")
    
    print(direccion)
