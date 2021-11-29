laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

def mi_metodo(self, nombre):
    print("{}.mi_metodo({}".format(self, nombre))

def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

def mostrar(self):
    print("Punto ({}, {}, {})".format(self.x, self.y, self.z))

#Punto = (x, y, z)

#p = Punto(1, 2, 3)
#p.mostrar()