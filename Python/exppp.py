def find_indegree(adj_matrix, n):
    indegree = [0] * n
    for j in range(n):
        sum_col = 0
        for i in range(n):
            sum_col += adj_matrix[i][j]
        indegree[j] = sum_col
    return indegree

def main():
    n = int(input("Enter number of vertices: "))
    adj_matrix = []

    print("Enter adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        adj_matrix.append(row)

    indegree = find_indegree(adj_matrix, n)
    print("Indegree:", ' '.join(map(str, indegree)))

    stack = []
    for i in range(n):
        if indegree[i] == 0:
            stack.append(i)

    res = []
    while stack:
        curr = stack.pop()
        res.append(curr)
        for j in range(n):
            if adj_matrix[curr][j] == 1:
                indegree[j] -= 1
                if indegree[j] == 0:
                    stack.append(j)

    # Convert numbers to letters (A, B, C...)
    vertex_labels = [chr(65 + i) for i in range(n)]

    if len(res) != n:
        print("Graph has a cycle. Topological sorting not possible.")
    else:
        topo_order = [vertex_labels[v] for v in res]
        print("Topological sorting:", ' → '.join(topo_order))

if __name__ == "__main__":
    main()
