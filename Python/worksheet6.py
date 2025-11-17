def find_subsets(S, target):
    n = len(S)
    result = []
    
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, n):
            path.append(S[i])
            backtrack(i + 1, path, current_sum + S[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result

# Input Data
S = [5, 7, 9, 11, 13]
d = 20

# Find all subsets
solutions = find_subsets(S, d)

# Display Results
if solutions:
    print(f"\nSubsets of {S} with sum {d}:")
    for subset in solutions:
        print(subset)
else:
    print("\nNo subset found with the given sum.")
