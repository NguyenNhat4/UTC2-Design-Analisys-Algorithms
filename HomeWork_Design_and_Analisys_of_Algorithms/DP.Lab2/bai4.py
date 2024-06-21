
arr = [1,2,3,2,1,5,6,1]

# not using DP 
def longest_wavio_sequence(nums):
    n = len(nums)
    max_length = 0
    start = n+1
    state = 0 

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            if state == 0: 
                start = i - 1
                state = 1
            elif state == -1:
                max_length = max(max_length, i - start)
                start = i - 1
                state = 1
        elif nums[i] < nums[i - 1]:
            if state == 1: 
                state = -1
    if start == n+1: 
        return None
    return max_length

# solve by dynamic programming
def DP_longest_wavio_sequence(nums):
    n = len(nums)
    inc = [1] * n
    decr = [1] * n
    max_length = 0
    for i in range(1,n):
        if nums[i] > nums[i - 1]:
            inc[i] = max(inc[i], inc[i-1]+1)
        elif nums[i] < nums[i - 1]:
            decr[i] = max(inc[i], decr[i-1]+1)
    for i in range(n):
        if inc[i] == 1 or inc[i] < inc[i+1]:
            continue
        else:
            j = i+1
            if j == n-1:
                return max(max_length, inc[i] + decr[j] - 1)
            while decr[j] < decr[j+1] and j < n-1:
                j+=1
            max_length = max(max_length, inc[i] + decr[j] - 1)
    return max_length

print(DP_longest_wavio_sequence(arr))
    



        

        
      
            



    

