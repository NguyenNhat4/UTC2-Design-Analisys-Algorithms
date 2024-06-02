def compare_meetings(meeting1, meeting2):
    return meeting1[1] - meeting2[1]

def max_number_of_meetings(start, end):
    n = len(start)
    dp = [0] * n
    dp[0]  = 1
    meetings = [(start[i], end[i]) for i in range(len(start))]
    for i in range (0,n):
        for j in range(0,i):
            if meetings[i][0] >= meetings[j][1]:
                dp[i] = max(dp[i],dp[j]+1)
     
    return dp[n-1]

a = [1, 3, 0, 5, 8, 5]
b = [2, 4, 6, 7, 9, 9]
result = max_number_of_meetings(a,b)
print(result) 
