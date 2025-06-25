import copy
import itertools

import networkx as nx

class Model:
    def __init__(self):
        self._idMap = {}
        for n in self.list1:
            self._idMap[n.id] = n


        self._graph = nx.Graph()
        self._graph = nx.DiGraph()

    def buildGraph(self):
        self._graph.clear()

        myedges = list(itertools.combinations(self.list_with_nodes,2))
        self._graph.add_edges_from(myedges)


    ### RICORSIONE
    def function_for_recursion(self):
        parziale = []
        self.best_prath = []
        self.best_sol = 0
        self.recursion(parziale)
        return

    def recursion(self, parziale):


        if :

            if total > self.best_sol:
                self.best_sol = total
                self.best_path = copy.deepcopy(parziale)


        for  in :
            if :
            parziale.append(a)
            self.ricorsione(parziale)
            parziale.pop()