
def max_number_of_meetings(start, end):
    n = len(start)
    dp = [0] * n
    dp[0]  = 1
 
    meetings = [(start[i], end[i]) for i in range(len(start))]
    meetings.sort(key=lambda x: x[1])
    for i in range (0,n):
        for j in range(0,i):
            if meetings[i][0] >= meetings[j][1]:
                dp[i] = max(dp[i],dp[j]+1)
     
    return dp[n-1]

a = [1, 3, 0, 5, 8, 5]
b = [5 ,4,2,7,10,6]
result = max_number_of_meetings(a,b)
print(result) 
