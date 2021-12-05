laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

muro = (0,1)

casillasmalas = ((laberinto[0])[1] , (laberinto[0])[2], (laberinto[0])[3], (laberinto[0])[4], (laberinto[1])[1], (laberinto[2])[1], (laberinto[2])[3], (laberinto[3])[3], (laberinto[4])[0], (laberinto[4])[1], (laberinto[4])[2], (laberinto[4])[3])


print(casillasmalas)

direccion = input("Selecciona a la dirección a la cual quieres ir: ARRIBA, ABAJO, IZQUIERDA, DERECHA")

if direccion == "ARRIBA":
    x = x - 1
    y = y
elif direccion == "ABAJO":
    x = x + 1
    y = y
elif direccion == "IZQUIERDA":
    x = x
    y = y + 1
elif direccion == "DERECHA":
    x = x
    y = y - 1