import copy
import itertools

import networkx as nx

class Model:
    def __init__(self):
        # definico tutte le istanze della classe
        self._idMap = {} # per risalire all'oggetto dal codice
        for n in self.list1:
            self._idMap[n.id] = n

        # definisco il grafo
        self._graph = nx.Graph() # grafo non orientato
        self._graph = nx.DiGraph() # grafo orientato

    def function_name1(self):
        # operazioni della prima funzione
        pass

    def function_name2(self):
        # operazioni della prima funzione
        pass

    def buildGraph(self):
        # aggiungo nodi e archi al grafo
        self._graph.clear()

        # Aggiungo un arco per ogni combinazione di nodi
        myedges = list(itertools.combinations(self.list_with_nodes,
                                              2))  # restituisce una lista di tuple con tutte le combinazioni dei nodi
        self._graph.add_edges_from(myedges)


    ### RICORSIONE
    def function_for_recursion(self):
        parziale = []
        self.best_prath = []
        self.best_sol = 0
        self.recursion(parziale)
        return

    def recursion(self, parziale): # tip: usare più funzioni per effettuare le verifiche
        # operazioni che svolgi sempre

        if : # condizione terminale

            if total > self.best_sol: # cerco la soluzione migliore
                self.best_sol = total
                self.best_path = copy.deepcopy(parziale) # necessario per copiare tutti gli oggetti di una lista

        # else: non è necessario
        for  in :
            if : # filtro per procedere nella ricerca
            parziale.append(a)
            self.ricorsione(parziale)
            parziale.pop() # Backtracking, necessario per esplorare tutti i percorsi