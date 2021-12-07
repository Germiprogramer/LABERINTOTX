laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

casillasmalas = ((laberinto[0])[1] , (laberinto[0])[2], (laberinto[0])[3], (laberinto[0])[4], (laberinto[1])[1], (laberinto[2])[1], (laberinto[2])[3], (laberinto[3])[3], (laberinto[4])[0], (laberinto[4])[1], (laberinto[4])[2], (laberinto[4])[3])

print((laberinto[0])[4])

print(casillasmalas)

x = 0
y = 0


print("Empiezas en la posición (0,0)")
print((laberinto[y])[x])

while (laberinto[y])[x] == ' ':
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
    if (laberinto[y])[x] == ' ':
        print("La casilla elegida NO es un muro, puede continuar en el laberinto")
    else:
        print("La casilla es un muro")
    
    print(direccion)

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

muro = "X"


def tablero(laberinto):
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
#cuando ponemos for i in range (12), nos referimos a los 12 primeros elementos de MURO????


print((laberinto[1])[1])

coordenadaslaberinto = (laberinto[y])[x]
casillasmalas = (laberinto[{}])[{}].format(muro)

def mi_metodo(self, nombre):
    print("{}.mi_metodo({}".format(self, nombre))

def __init__(self, x, y):
    self.x = x
    self.y = y

def mostrar(self):
    print("Punto ({}, {})".format(self.x, self.y))


tablero(laberinto)

#DUDA: COMO HAGO PARA QUE ME SAQUE UNA SOLA CASILLA, Y NO LA FILA COMPLETA


#Punto = (x, y)
#p = Punto(1, 2)
#p.mostrar()
    

print("BIENVENIDO AL LABERINTO \nSELEECIONE LA DIFICULTAD A LA QUE DESEA JUGAR: 1, 2")
dificultad = input()

if dificultad == 1:
    print("Ha seleccionado la dificultad 1. COMIENZA EL JUEGO")
    laberinto = [
         ['camino', 'X', 'X', 'X', 'X'], 
         ['camino', 'X', 'camino', 'camino', 'camino'],
         ['camino', 'X', 'camino', 'X', 'camino'], 
         ['camino', 'camino', 'camino', 'X', 'camino'], 
         ['X', 'X', 'X', 'X', 'S']
         ]
elif dificultad == 2:
    print("Ha seleccionado la dificultad 2. COMIENZA EL JUEGO")
    laberinto = [
        ['camino', 'camino', 'camino', 'X', 'X', 'S', 'camino', 'X', 'X']
        ['X', 'X', 'camino', 'X', 'X', 'X', 'camino', 'X', 'X']
        ['camino', 'camino', 'camino', 'X', 'X', 'X', 'camino', 'X', 'X']
        ['camino', 'X', 'X', 'X', 'X', 'X', 'camino', 'camino', 'X']
        ['camino', 'camino', 'camino', 'X', 'X', 'X', 'X', 'camino', 'X']
        ['camino', 'X', 'camino', 'camino', 'camino', 'X', 'X', 'camino', 'X']
        ['camino', 'camino', 'camino', 'X', 'camino', 'X', 'camino', 'camino', 'X']
        ['X', 'X', 'X', 'X', 'camino', 'X', 'camino', 'X', 'X']
        ['X', 'X', 'X', 'X', 'camino', 'camino', 'camino', 'X', 'X']
    ]