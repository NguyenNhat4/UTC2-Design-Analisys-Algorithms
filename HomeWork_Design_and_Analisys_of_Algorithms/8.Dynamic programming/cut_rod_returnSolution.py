def memoized_cut_rod(p, n):
    r = [-float('inf')] * (n+1)  
    return memoized_cut_rod_aux(p, n, r, s)

def memoized_cut_rod_aux(p, n, r, s):
    if r[n] >= 0: 
        return r[n], s[n]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n+1):
            temp, temp_s = memoized_cut_rod_aux(p, n - i, r, s)
            if p[i-1] + temp > q:
                q = p[i-1] + temp
                s[n] = i  
    r[n] = q 
    return q, s[n]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 7
value, solution = memoized_cut_rod(p, n)
print("Optimal value:", value)
print("Optimal solution:", solution)
