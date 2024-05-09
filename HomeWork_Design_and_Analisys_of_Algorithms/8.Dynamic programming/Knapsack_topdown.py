W = [2,1,3,2]
V = [12,10,20,15]
n = 5
def initizalizeTableF(numRow,numCol, initValue):
    return [[initValue]*numCol for _ in range(numRow)]

F = initizalizeTableF(5,n+1,-1)

for i in range (n+1):
    F[0][i] = 0
for i in range (n):
    F[i][0] = 0


def MFKnapsack(i,j):
    if F[i][j] < 0:
        if j  < W[i-1]:
            value =  MFKnapsack(i-1,j) 
        else:
            value = max( MFKnapsack(i-1,j), V[i-1 ] + MFKnapsack(i-1,j-W[i-1]))  
            # check if putting this item in plus the remains is greater or not 
        F[i][j] = value 
    return F[i][j]


MFKnapsack(4,5)

for i in F:
    print(' '.join(map(str, i)))
