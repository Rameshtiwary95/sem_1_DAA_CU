import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    pq = [(0, source)]  
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 1)],
    'C': [('A', 2), ('B', 5), ('D', 8)],
    'D': [('B', 1), ('C', 8)]
}

source = 'A'
shortest_paths = dijkstra(graph, source)

print(f"Shortest paths from {source}:")
for node, dist in shortest_paths.items():
    print(f"{source} → {node} = {dist}")
