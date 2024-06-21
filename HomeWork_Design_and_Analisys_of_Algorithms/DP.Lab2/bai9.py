def partition_candies(N, A):
    total_sum = sum(A)
    half_sum = total_sum // 2

    # Initialize DP table
    dp = [[0] * (half_sum + 1) for _ in range(N + 1)]
    for i in range(1,N+1):
        for j in range (half_sum+1):
            if A[i-1] <= j:
                dp[i][j] = max(dp[i-1][j - A[i-1]] + A[i-1],     dp[i-1][j] )
            else: 
                dp[i][j] = dp[i-1][j] 
    for i in dp:
        print(i,end="\n")
    first_list = []
    s = dp[N][half_sum]

    
    for i in range(N,0,-1):
        if dp[i][s] != dp[i - 1][s]:
            first_list.append(A[i-1])
            s -= A[i-1]
        

    difference = abs( (total_sum - dp[N][half_sum]) - dp[N][half_sum])
    return len(first_list) , difference ,first_list[::-1]



        




# Example usage
N = 5
A = [8, 7, 6, 5, 4]
number_of_boxes, difference, first_child_boxes = partition_candies(N, A)
print(f"Number of boxes given to the first child: {number_of_boxes}")
print(f"Difference of candies between the two children: {difference}")
print(f"List of boxes given to the first child: {first_child_boxes}")
