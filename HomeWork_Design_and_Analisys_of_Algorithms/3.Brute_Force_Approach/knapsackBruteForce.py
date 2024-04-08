def knapsack_bruteforce(values, weights, capacity):
    n = len(values)
    max_value = 0
    best_subset = None

   
    for i in range(2 ** n):
        subset_value = 0
        subset_weight = 0
        subset = []
        
        for j in range(n):
            if (i >> j) & 1:
                subset_value += values[j]
                subset_weight += weights[j]
                subset.append(j)
        
        if subset_weight <= capacity and subset_value > max_value:
            max_value = subset_value
            best_subset = subset
    
    return max_value, best_subset

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, best_subset = knapsack_bruteforce(values, weights, capacity)
print("Maximum value:", max_value)
print("Items in the knapsack:", best_subset)

