laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

muro = "X"

i = 0
j = 0
k = 0

def tablero(laberinto):
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
#cuando ponemos for i in range (12), nos referimos a los 12 primeros elementos de MURO????
    for i in range (12):
        laberinto[muro[i][0]][muro[i][1]]
    for i in range (5):
        print[laberinto[i]]




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