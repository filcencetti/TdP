### PERCORSO PIù LUNGO IN TERMINI DI ARCHI (SENZA CONSIDERARE IL PESO)
# SI PUò AGGIUNGERE UN ARCO SOLO SE IL SUO PESO è MAGGIORE DI TUTTI I PESI GIà PRESENTI
def searchPath(self, product_number):
    nodoSource = self.idMap[product_number]
    parziale = []
    self.ricorsione(parziale, nodoSource, 0)
    print("final", len(self._solBest), [i[2]["weight"] for i in self._solBest])

def ricorsione(self, parziale, nodoLast, livello):
    archiViciniAmmissibili = self.getArchiViciniAmm(nodoLast, parziale)

    if len(archiViciniAmmissibili) == 0:
        if len(parziale) > len(self._solBest):
            self._solBest = list(parziale)
            print(len(self._solBest), [ii[2]["weight"] for ii in self._solBest])

    for a in archiViciniAmmissibili:
        parziale.append(a)
        self.ricorsione(parziale, a[1], livello + 1)
        parziale.pop()

def getArchiViciniAmm(self, nodoLast, parziale):
    archiVicini = self._grafo.edges(nodoLast, data=True)
    result = []
    for a1 in archiVicini:
        if self.isAscendent(a1, parziale) and self.isNovel(a1, parziale):
            result.append(a1)
    return result

def isAscendent(self, e, parziale):
    if len(parziale) == 0:
        print("parziale is empty in isAscendent")
        return True
    return e[2]["weight"] >= parziale[-1][2]["weight"]

def isNovel(self, e, parziale):
    if len(parziale) == 0:
        print("parziale is empty in isnovel")
        return True
    e_inv = (e[1], e[0], e[2])
    return (e_inv not in parziale) and (e not in parziale)