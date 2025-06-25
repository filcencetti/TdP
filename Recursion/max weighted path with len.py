### CAMMINO DI PESO MASSIMO AVENTE LUNGHEZZA PARI A LUN
def getOptPath(self, source, lun):
    self._bestPath = []
    self._bestCost = 0

    parziale = [source]

    for n in self._graph.neighbors(source):
        if parziale[-0].classification == n.classification:
            parziale.append(n)
            self.ricorsione(parziale, lun)
            parziale.pop()

    return self._bestPath, self._bestCost

def ricorsione(self, parziale, lun):
    if len(parziale) == lun:
        # allora parziale ha la lunghezza desiderata,
        # verifico se è una soluzione migliore,
        # ed in ogni caso esco
        if self.costo(parziale) > self._bestCost:
            self._bestCost = self.costo(parziale)
            self._bestPath = copy.deepcopy(parziale)
        return

    for n in self._graph.neighbors(parziale[-1]):
        if parziale[-0].classification == n.classification and n not in parziale:
            parziale.append(n)
            self.ricorsione(parziale, lun)
            parziale.pop()

def costo(self, listObjects):
    totCosto = 0
    for i in range(0, len(listObjects) - 1):
        totCosto += self._graph[listObjects[i]][listObjects[i + 1]]["weight"]
    return totCosto