import java.util.*;

public class MergeSortExample {

    // Merge Sort function
    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }

        int mid = arr.length / 2;

        // Split into left and right
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);

        // Recursive sort
        left = mergeSort(left);
        right = mergeSort(right);

        // Merge
        return merge(left, right);
    }

    // Merge two sorted arrays
    public static int[] merge(int[] left, int[] right) {
        List<Integer> result = new ArrayList<>();

        int i = 0, j = 0;

        // Compare and merge
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                result.add(left[i]);
                i++;
            } else {
                result.add(right[j]);
                j++;
            }
        }

        // Add remaining elements
        while (i < left.length) {
            result.add(left[i]);
            i++;
        }
        while (j < right.length) {
            result.add(right[j]);
            j++;
        }

        // Convert List<Integer> to int[]
        return result.stream().mapToInt(Integer::intValue).toArray();
    }

    // Main function
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 6};
        System.out.println("Original: " + Arrays.toString(arr));

        int[] sorted = mergeSort(arr);
        System.out.println("Sorted: " + Arrays.toString(sorted));
    }
}
