import java.util.*;

public class QuickSort {

    // Partition function
    public static int partition(int a[], int lb, int ub) {
        int pivot = a[lb];
        int start = lb;
        int end = ub;

        while (start < end) {
            while (start <= ub && a[start] <= pivot) {
                start++;
            }
            while (end >= lb && a[end] > pivot) {
                end--;
            }
            if (start < end) {
                // swap a[start] and a[end]
                int temp = a[start];
                a[start] = a[end];
                a[end] = temp;
            }
        }

        // Swap pivot with a[end]
        int temp = a[lb];
        a[lb] = a[end];
        a[end] = temp;

        return end;
    }

    // QuickSort function
    public static void quickSort(int a[], int lb, int ub) {
        if (lb < ub) {
            int loc = partition(a, lb, ub);
            quickSort(a, lb, loc - 1);
            quickSort(a, loc + 1, ub);
        }
    }

    // Main function
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("Before Sorting:");
        for (int i : arr) {
            System.out.print(i + " ");
        }

        quickSort(arr, 0, arr.length - 1);

        System.out.println("\nAfter Sorting:");
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
