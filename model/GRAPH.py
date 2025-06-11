import copy

import networkx as nx

## Creare un grafo
nx.Graph() # non orientato
nx.DiGraph() # orientato

# Comandi su nodi e archi
self._graph[nodo1][nodo2] # restituisce gli attributi dell'arco (es: {"weight":5})
self._graph.nodes() # restituisce una lista di nodi
self._graph.edges() # restituisce una lista di archi
self._graph.has_edge(node1,node2) # ritorna True se esiste un arco che collega i due nodi, False altrimenti
nx.node_connected_component(self._graph, node) # ritorna una lista di utti i nodi raggiungibili da node (solo con archi non orientati)

# Depth First Search --> visita ogni percorso fino in fondo e torna indietro
nx.dfs_tree(self._graph[])
nx.dfs_tree(self._graph[],node_source) # restituisce un grafo con tutti i nodi e archi raggiungibili partendo dal node_source

# Breadth First Search --> visita i nodi a livelli (per grado)
nx.bfs_tree(self._graph[]) # GRAFO NON PESATO
nx.bfs_tree(self._graph[],node_source) # restituisce un grafo con tutti i nodi e archi raggiungibili partendo dal node_source

### DFS e BFS visitano gli stessi nodi ma non gli stessi archi

# Percorso più corto (minimo peso totale) tra due nodi
nx.shortest_path(self._graph, nodo1, nodo2)
nx.dijkstra_path(self._graph, nodo1, nodo2, weight = "weight") # Archi con peso positivo

# Tutti i percorsi più corti da tutte i nodi sorgente
nx.floyd_warshall(self._graph,weight = "weight") # Assenza di cicli negativi

# Soluzione al percorso più corto da un singolo nodo sorgente
nx.all_pairs_bellman_ford_path(self._graph,weight = "weight" ) # Assenza di cicli negativi

# Cammino euleriano
nx.is_eulerian(self._graph) # Ritorna True se il grafo è euleriano

# Cammino Hamiltoniano (percorso che passa per tutti i vertici una volta sola)
nx.hamiltonian_path(self._graph)

# Algoritmo di Christofides (alternativa al comando hamiltonian_path)
nx.christofides(self._graph, weight = "weight")

# Percorso più lungo
lp = []
tree = nx.dfs_tree(self._graph, node_source)
nodes = list(tree.nodes())
for node in nodes:
    tmp = [node]
    while tmp[0] != node_source:
        pred = nx.predecessor(tree, node_source, tmp[0])
        tmp.insert(0, pred[0])
    if len(tmp) > len(lp):
        lp = copy.deepcopy(tmp)