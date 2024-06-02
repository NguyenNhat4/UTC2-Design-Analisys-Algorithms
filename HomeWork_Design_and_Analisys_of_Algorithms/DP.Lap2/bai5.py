

# 1.dp[i][w] represents the maximum weight that can be achieved with the first i items and weight limit w.
# 2.We build the dp table where dp[i][w] is computed as the maximum value of either including the i-th item (if it fits) or not including it.
# 3.After constructing the dp table, we trace back to find which items are included in the optimal solution.

def knapsack(n, W, weights):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + weights[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    max_weight = dp[n][W]
    selected_items = []
    w = W

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i)
            w -= weights[i-1]

    selected_items.reverse()

    return max_weight, selected_items



# input
n = 4
W = 13
weights = [2, 3, 4, 5]

max_weight, selected_items = knapsack(n, W, weights)

print( max_weight)
print( selected_items)
