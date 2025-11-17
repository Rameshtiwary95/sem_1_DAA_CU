// import java.util.*;

// class GFG{

//     private static void
//     topologicalSortUtil(int v, List<Integer>[] adj,
//       boolean[] visited,
//          Stack<Integer> stack)
//     {
//         visited[v] = true;

//         for (int i : adj[v]) {
//             if (!visited[i]) {
//              topologicalSortUtil(i, adj, visited, stack);
//             }
//         }

//         stack.push(v);
//     }
//     static List<Integer>[] constructadj(int V,
//            int[][] edges)
//     {

//         List<Integer>[] adj = new ArrayList[V];

//         for (int i = 0; i < V; i++) {
//             adj[i] = new ArrayList<>();
//         }

//         for (int[] edge : edges) {
//             adj[edge[0]].add(edge[1]);
//         }
//         return adj;
//     }
//     static int[] topologicalSort(int V, int[][] edges)
//     {
//         Stack<Integer> stack = new Stack<>();
//         boolean[] visited = new boolean[V];

//         List<Integer>[] adj = constructadj(V, edges);
//         for (int i = 0; i < V; i++) {
//             if (!visited[i]) {
//                 topologicalSortUtil(i, adj, visited, stack);
//             }
//         }

//         int[] result = new int[V];
//         int index = 0;
//         while (!stack.isEmpty()) {
//             result[index++] = stack.pop();
//         }

//         return result;
//     }

//     public static void main(String[] args)
//     {
//         int v = 6;
//         int[][] edges = {{2, 3}, {3, 1}, {4, 0},
//                           {4, 1}, {5, 0}, {5, 2}};

//         int[] ans = topologicalSort(v, edges);

//         for (int node : ans) {
//             System.out.print(node + " ");
//         }
//         System.out.println();
//     }
// }



import java.util.*;

public class SimpleTopo {
    // DFS helper function
    private static void dfs(int v, List<Integer>[] adj, boolean[] visited, Stack<Integer> stack) {
        visited[v] = true;
        for (int u : adj[v]) {
            if (!visited[u]) {
                dfs(u, adj, visited, stack);
            }
        }
        stack.push(v); // Push after visiting all neighbours
    }

    // Function for topological sort
    public static void topologicalSort(int V, int[][] edges) {
        // adjacency list
        List<Integer>[] adj = new ArrayList[V];
        for (int i = 0; i < V; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) adj[e[0]].add(e[1]);

        boolean[] visited = new boolean[V];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < V; i++) {
            if (!visited[i]) dfs(i, adj, visited, stack);
        }

        // Print result
        System.out.print("Topological Order: ");
        while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }
    }

    public static void main(String[] args) {
        int V = 6; // number of vertices
        int[][] edges = {
            {5, 2}, {5, 0}, {4, 0}, {4, 1}, {2, 3}, {3, 1}
        };

        topologicalSort(V, edges);
    }
}
