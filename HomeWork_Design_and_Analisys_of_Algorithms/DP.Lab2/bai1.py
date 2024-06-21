def LIS(arr):
    n = len(arr)
    LIS = [1]*len(arr)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[i] > arr[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)
                
                

arr  = [2,3,4,1,3]

print(f"long increasing subsequence is {LIS(arr)}")