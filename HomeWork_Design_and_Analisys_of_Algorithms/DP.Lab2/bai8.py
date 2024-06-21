N= 4
M= 11
A = [5,1,8,6]


def CoinChange(A,M,N):
    A.sorted()
    C = [[0]*(N) for _ in range(M+1)]   
    for i in range(1,N):
        for j in range(1,M):
            if j >= A[i]:
                C[i][j] = min(C[i-1][j], 1+C[i][j-i])
            else:
                C[i][j] = C[i-1][j] 
    min = C[N-1][M]
    x = N-1
    y = M
    while  min == 0:
        if C[x][y] != C[x-1][y]:
            min -= C[x][y]
            print(f"{num} xu {x} dong")
            y-= x
        else:
            x-=1

        







