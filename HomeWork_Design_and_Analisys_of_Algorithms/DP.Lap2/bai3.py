def thuê_máy(n, start, end, cost):
    Lend_Computers = [(start[i], end[i], cost[i]) for i in range(n)]
    def sort_by_end_time(meeting):
        return meeting[1]
    
    Lend_Computers.sort(key=sort_by_end_time)

    def find_last_non_conflict(Lend_Computers, i):
        for j in range(i - 1, -1, -1):
            if Lend_Computers[j][1] <= Lend_Computers[i][0]:
                return j
        return None # if can't not find any

    def max_rental_dp(Lend_Computers):
        dp = [0] * n 
        dp[0] = Lend_Computers[0][2] # assign first element to first profit in 

        for i in range(1, n):
            incl_profit = Lend_Computers[i][2]
            l = find_last_non_conflict(Lend_Computers, i)
            if l is not None:
                incl_profit += dp[l]

            excl_profit = dp[i - 1]

            dp[i] = max(incl_profit, excl_profit)

        return dp[n - 1]

    return max_rental_dp(Lend_Computers)

n = 4
start_times = [1, 3, 0, 5]
end_times = [2, 4, 6, 7]
costs = [50, 20, 100, 200]
print(thuê_máy(n, start_times, end_times, costs))
