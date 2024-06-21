start = [1,5,2,6,7]
end = [5,4,7,2,9]
profit = [1,2,3,4,5] 

def max_profit_for_lending_machine(n,start,end,profit):
    lending_list = [(start[i],end[i],profit[i]) for i in range(n)]
    lending_list.sort(key=lambda x: x[1])
    dp = [0]*n
    dp[0] = lending_list[0][2]
    def last_none_conflicts(i,lending_list):
        for k in range(i-1,-1,-1):
            if lending_list[i][0] >= lending_list[k][1]:
                return k
        return None
    
    for i in range(1,n):
        inc = lending_list[i][2]
        l = last_none_conflicts(i,lending_list)
        if l is not None:
            inc += dp[l]
        dp[i] = max(inc, dp[i-1])


    return dp[n-1]



print(max_profit_for_lending_machine(len(start),start,end,profit))





