import heapq

def dijkstra(graph, start):
    # graph = adjacency list {u: [(v, weight), ...]}
    # start = source node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # priority queue (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip if we already found a shorter path
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example Graph (Adjacency List)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3), ('E', 4)],
    'D': [('B', 10), ('C', 3), ('E', 6)],
    'E': [('C', 4), ('D', 6)]
}

source = 'A'
print(f"Shortest paths from {source}:")
print(dijkstra(graph, source))
