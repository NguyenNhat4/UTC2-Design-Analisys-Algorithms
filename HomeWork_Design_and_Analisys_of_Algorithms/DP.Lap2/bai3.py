def thuê_máy(n, start, end, cost):
    meetings = [(start[i], end[i], cost[i]) for i in range(n)]
    meetings.sort(key=lambda x: x[1])

    def find_last_non_conflict(meetings, i):
        for j in range(i - 1, -1, -1):
            if meetings[j][1] <= meetings[i][0]:
                return j
        return None
    def max_rental_dp(meetings):
        dp = [0] * n
        dp[0] = meetings[0][2]

        for i in range(1, n):
            incl_profit = meetings[i][2]
            l = find_last_non_conflict(meetings, i)
            if l is not None:
                incl_profit += dp[l]

            excl_profit = dp[i - 1]

            dp[i] = max(incl_profit, excl_profit)

        return dp[n - 1]

    return max_rental_dp(meetings)



# input
n = 4
start_times = [1, 3, 0, 5]
end_times = [2, 4, 6, 7]
costs = [50, 20, 100, 200]
print(thuê_máy(n, start_times, end_times, costs))  # Output: 250
