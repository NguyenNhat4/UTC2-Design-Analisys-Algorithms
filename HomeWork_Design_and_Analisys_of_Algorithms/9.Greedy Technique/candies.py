# https://www.hackerrank.com/challenges/candies/problem

def candies(n, arr):
   
    k = [1]*n
    for i in range (1,len(arr)):
        if arr[i] > arr[i-1]:
            k[i] = k[i-1]+ 1
        
    for i in range(n-2,-1,-1):
        if arr[i] > arr[i+1]:
            k[i] = max(k[i], k[i+1] + 1)

    return sum(k)   
