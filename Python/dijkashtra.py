import sys

def dijkstra(graph, src):
    V = len(graph)
    dist = [sys.maxsize] * V   # shortest distance from src to each vertex
    dist[src] = 0
    sptSet = [False] * V       # Shortest Path Tree Set

    for _ in range(V):
        # Pick the vertex with the minimum distance not yet processed
        u = min_distance(dist, sptSet)
        sptSet[u] = True

        # Update distance values of adjacent vertices
        for v in range(V):
            if (graph[u][v] > 0 and not sptSet[v] and
               dist[u] + graph[u][v] < dist[v]):
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist, src)

def min_distance(dist, sptSet):
    min_val = sys.maxsize
    min_index = -1
    for v in range(len(dist)):
        if not sptSet[v] and dist[v] < min_val:
            min_val = dist[v]
            min_index = v
    return min_index

def print_solution(dist, src):
    print(f"Vertex \t Distance from Source {src}")
    for i in range(len(dist)):
        print(f"{i} \t {dist[i]}")

# Example graph (adjacency matrix)
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

dijkstra(graph, 0)
