

# Require 2^n-1 function calls
# version 1
def cut_rod(p, n):
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = [-float('inf')] * (n+1)  
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:  # If the solution for length n is already known
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n+1):
            q = max(q, p[i-1] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q  # Remember the solution value for length n
    return q

def bottom_up_cut_rod(p, n):
    r = [0] * (n+1)  # Initialize an array to store solutions
    for j in range(1, n+1):
        q = -float('inf')
        for i in range(1, j+1):
            q = max(q, p[i-1] + r[j - i])
        r[j] = q  # Remember the solution value for length j
    return r[n]

# Example usage:
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 4
print(memoized_cut_rod(p, n))
print(bottom_up_cut_rod(p, n))
