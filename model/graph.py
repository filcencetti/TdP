import networkx as nx

## Creare un grafo
nx.Graph() # non orientato
nx.DiGraph() # orientato

# Comandi su nodi e archi
self._graph[nodo1][nodo2] # restituisce gli attributi dell'arco (es: {"weight":5})
self._graph.nodes() # restituisce una lista di nodi
self._graph.edges() # restituisce una lista di archi

# Depth First Search
nx.dfs_tree(self._graph[])

# Breadth First Search
nx.bfs_tree(self._graph[]) # Grafo non pesato

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