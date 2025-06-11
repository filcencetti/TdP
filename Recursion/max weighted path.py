### CAMMINO DI PESO MASSIMO CON VINCOLO: PESO ARCHI DECRESCENTE
def getBestPath(self, startStr):
    self._bestPath = []
    self._bestScore = 0

    start = self._idMap[int(startStr)]

    parziale = [start]

    vicini = self._graph.neighbors(start)
    for v in vicini:
        parziale.append(v)
        self.ricorsione(parziale)
        parziale.pop()

    return self._bestPath, self._bestScore


def ricorsione(self, parziale):
    if self.getScore(parziale) > self._bestScore:
        self._bestScore = self.getScore(parziale)
        self._bestPath = copy.deepcopy(parziale)

    for v in self._graph.neighbors(parziale[-1]):
        if (v not in parziale and  # check if not in parziale
                self._graph[parziale[-2]][parziale[-1]]["weight"] >
                self._graph[parziale[-1]][v]["weight"]):  # check if peso nuovo arco è minore del precedente
            parziale.append(v)
            self.ricorsione(parziale)
            parziale.pop()


