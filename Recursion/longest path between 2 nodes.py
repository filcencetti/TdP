### PERCORSO CHE MASSIMIZZI LA SOMMA DEI PESI TRA DUE NODI

def getCamminoOttimo(self, v0, v1, t):
    self._bestPath = []
    self._bestObjFun = 0

    parziale = [v0]

    self.ricorsione(parziale, v1, t)

    return self._bestPath, self._bestObjFun

def ricorsione(self, parziale, v1, t):
    # Verificare se parziale è una possibile soluzione
    # verificare se parziale è meglio del best
    # esco
    if parziale[-1] == v1:
        if self.getObjFun(parziale) > self._bestObjFun:
            self._bestObjFun = self.getObjFun(parziale)
            self._bestPath = copy.deepcopy(parziale)

    if len(parziale) == t + 1:
        return

    # Posso ancora aggiungere nodi: prendo i vicini e aggiungo un nodo alla volta
    for n in self._graph.neighbors(parziale[-1]):
        if n not in parziale:
            parziale.append(n)
            self.ricorsione(parziale, v1, t)
            parziale.pop()

def getObjFun(self, listOfNodes):
    objval = 0
    for i in range(0, len(listOfNodes) - 1):
        objval += self._graph[listOfNodes[i]][listOfNodes[i + 1]]["weight"]
    return objval
