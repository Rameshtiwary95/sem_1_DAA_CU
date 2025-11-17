inf = float('inf')

def floyd_warshall_algo(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print("\nFinal Shortest Path Matrix:")
    for i in range(n):
        for j in range(n):
            print(0 if dist[i][j] == inf else dist[i][j], end="\t")
        print()

v = int(input("Enter total number of vertices: "))
print("Enter adjacency matrix (use 'inf' for no direct connection):")

graph = []
for i in range(v):
    row_input = input().split()
    if len(row_input) != v:
        exit()
    row = [inf if val.lower() == 'inf' else int(val) for val in row_input]
    graph.append(row)

floyd_warshall_algo(graph)
