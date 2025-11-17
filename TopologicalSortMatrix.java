import java.util.*;

public class TopologicalSortMatrix {

    // Function to calculate indegree of each vertex
    static void findIndegree(int[][] a, int[] indegree, int n) {
        for (int j = 0; j < n; j++) {
            int sum = 0;
            for (int i = 0; i < n; i++) {
                sum += a[i][j];
            }
            indegree[j] = sum;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input number of vertices
        System.out.print("Enter no. of vertices: ");
        int n = sc.nextInt();

        int[][] a = new int[100][100];
        int[] indegree = new int[100];
        int[] stack = new int[100];
        int[] res = new int[100];
        int top = -1, k = 0;

        // Input adjacency matrix
        System.out.println("Enter adjacency matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = sc.nextInt();
            }
        }

        // Find indegree
        findIndegree(a, indegree, n);

        System.out.print("Indegree: ");
        for (int i = 0; i < n; i++) {
            System.out.print(indegree[i] + " ");
        }

        // Push vertices with indegree 0 into stack
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                stack[++top] = i;
            }
        }

        // Perform Topological Sort
        while (top != -1) {
            int curr = stack[top--];
            res[k++] = curr;

            for (int j = 0; j < n; j++) {
                if (a[curr][j] == 1) {
                    indegree[j]--;
                    if (indegree[j] == 0) {
                        stack[++top] = j;
                    }
                }
            }
        }

        // Print result
        System.out.print("\nTopological sorting: ");
        for (int i = 0; i < n; i++) {
            System.out.print(res[i] + " ");
        }

        sc.close();
    }
}
