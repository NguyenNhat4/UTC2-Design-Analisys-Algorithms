def assignment_bruteforce(costs):
    n = len(costs)
    min_cost = float('inf')
    best_assignment = None

    # Generate all possible permutations of assignments
    for permutation in generate_permutations(n):
        total_cost = 0
        for i in range(n):
            total_cost += costs[i][permutation[i]]
        if total_cost < min_cost:
            min_cost = total_cost
            best_assignment = permutation

    return min_cost, best_assignment

def generate_permutations(n):
    if n == 0:
        return [[]]
    else:
        permutations = []
        for i in range(n):
            rest = list(range(i)) + list(range(i+1, n))
            for p in generate_permutations(n-1):
                permutations.append([i] + [rest[j] for j in p])
        return permutations

# Example usage:
costs = [[10, 20, 30],
         [40, 50, 60],
         [70, 80, 90]]
min_cost, best_assignment = assignment_bruteforce(costs)
print("Minimum cost:", min_cost)
print("Best assignment:", best_assignment)

