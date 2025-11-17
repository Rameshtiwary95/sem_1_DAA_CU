import sys

def primMST(graph):
    V = len(graph)  # Number of vertices

    # Array to store constructed MST
    parent = [-1] * V

    # Key values used to pick minimum weight edge
    key = [sys.maxsize] * V

    # To represent set of vertices included in MST
    mstSet = [False] * V

    # Start with the first vertex
    key[0] = 0
    parent[0] = -1  # First node is always the root of MST

    for _ in range(V):
        # Pick the minimum key vertex not in mstSet
        u = min_key_vertex(key, mstSet)
        mstSet[u] = True

        # Update key values of adjacent vertices
        for v in range(V):
            if graph[u][v] != 0 and mstSet[v] == False and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    printMST(parent, graph)

def min_key_vertex(key, mstSet):
    min_val = sys.maxsize
    min_index = -1
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def printMST(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(graph)):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

# Example graph as adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

primMST(graph)
