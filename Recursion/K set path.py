### insieme di K oggetti
def getDreamTeam(self, k):
    self._bestPath = []
    self._bestScore = 1000

    parziale = []
    self.ricorsione(parziale, k)
    return self._bestPath, self._bestScore


def ricorsione(self, parziale, k):
    if len(parziale) == k:
        if self.getScore(parziale) < self._bestScore:
            self._bestScore = self.getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)
        return

    for n in self._graph.nodes():
        if n not in parziale:
            parziale.append(n)
            self.ricorsione(parziale, k)
            parziale.pop()

def getScore(self, team): # la somma degli oggetti nell'insieme è la somma dei pesi con gli oggetti fuori dall'insieme
        score = 0
        for e in self._graph.edges(data=True):
            if e[0] not in team and e[1] in team:
                score += e[2]["weight"]
        return score