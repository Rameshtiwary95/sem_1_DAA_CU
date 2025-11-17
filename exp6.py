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


S = [5, 7, 9, 11, 13]
d = 20

solutions = find_subsets(S, d)

if solutions:
    print(f"Subsets of {S} with sum {d}:")
    for subset in solutions:
        print(subset)
else:
    print("No subset found with the given sum.")
