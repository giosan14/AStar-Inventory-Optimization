import os

class grafoA(object):
  
    def __init__(self):
        self.num_obs = int(input('Numero de obstaculos que hay: '))
        self.group_obs = []
        for i in range (self.num_obs):
            self.single_obs = []
            print(' Obstaculo ', i+1)
            x_vector = int(input('Posicion en Y (Renglon) del obstaculo: '))
            y_vector = int(input('Posicion en X (Columna) del obstaculo: '))
            self.single_obs.append((x_vector, y_vector))
            self.group_obs.append(self.single_obs)
        
    def heuristica(self, inicio, fin):
        total = 0
        for i in range(len(inicio)):
            diff = inicio[i] - fin[i]
            total = total + abs(diff)
        D = total  
        return D        


    def obtenerVecinos(self, pos):
        n = []
        z = 0
        for dx, dy in [(1,0),(0,1),(0,-1),(-1,0)]:
            z += 1
            x2 = pos[0] + dx
            y2 = pos[1] + dy

            if x2 < 0 or x2 > 4 or y2 < 0 or y2 > 4:
                continue
            n.append((x2, y2))
        return n
    
    def move_cost(self, a, b):
        for obstaculo in self.group_obs:
            if b in obstaculo:
                return 100
        return 1
    
def ABusqueda(inicio, fin, graph):
    G = {}
    F = {}
    G[inicio] = 0
    F[inicio] = graph.heuristica(inicio, fin)

    lista_cerrada = set()
    lista_abierta = set([inicio])

    antecesor = {}

    while len(lista_abierta) > 0:
        actual = None
        actualFscore = None
        for pos in lista_abierta:
            if actual is None or F[pos] < actualFscore:
                actualFscore = F[pos]
                actual = pos

        if actual == fin:
            path = [actual]
            while actual in antecesor:
                actual = antecesor[actual]
                path.append(actual)
            path.reverse()
            return path, F[fin]
        lista_abierta.remove(actual)
        lista_cerrada.add(actual)
        
        print("lista abierta", lista_abierta)
        print("lista cerrada", lista_cerrada)

        for vecino in graph.obtenerVecinos(actual):
            if vecino in lista_cerrada:
                continue
            alternativaG = G[actual] + graph.move_cost(actual, vecino)
                
            if vecino not in lista_abierta:
                lista_abierta.add(vecino)
            elif alternativaG >= G[vecino]:
                continue

            antecesor[vecino] = actual
            G[vecino] = alternativaG
            H = graph.heuristica(vecino, fin)
            
            #FUNCION
            F[vecino] = G[vecino] + H
            print("Funcion [F]", F[vecino])
    raise RuntimeError("No encontro solucion")


if __name__ == "__main__":
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

    graph =  grafoA()
    print('Posicion del robot')
    xR  = int(input("Posicion en Y (Renglon) del robot = "))
    yR  = int(input("Posicion en X (Columna) de robot = "))

    mercancias = []
    for i in range(0, 3, 1):
        n = []
        print ('Mercancia: ', i+1)
        xI = int(input("Ingrese posicion en Y (Renglon) inicial = "))
        yI = int(input("Ingrese posicion en X (Columna) inicial = "))

        xF = int(input("Ingrese posicion en Y (Renglon) final = "))
        yF = int(input("Ingrese posicion en X (Columna) final = "))
        n.append((xI, yI))
        n.append((xF, yF))
        mercancias.append(n)


    z = 0
    for n in mercancias:
        inicio = n[0]
        fin = n[1]

        print('Movimiento Robot a Mercancia')
        result, cost = ABusqueda((xR, yR), (inicio[0], inicio[1]), graph)
        print("---RUTA---", result)
        print("---COSTO---", cost)
        xR = inicio[0]
        yR = inicio[1]

        print('Moviendo mercancia ', z+1)
        print('Posicion robot:',xR,',', yR)
        print('Inicio:', inicio, 'Fin:', fin)
        result, cost = ABusqueda((xR, yR), (fin[0], fin[1]), graph)
        print("---RUTA---", result)
        print("---COSTO---", cost)
        xR = fin[0]
        yR = fin[1]

        z += 1
else: print("error")
