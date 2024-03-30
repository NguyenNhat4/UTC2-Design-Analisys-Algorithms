# Let A[0..n − 1] be an array of n real numbers. A pair (A[i], A[j ]) is said to
# be an inversion if these numbers are out of order, i.e., i < j but A[i] > A[j ].
# Design an O(n log n) algorithm for counting the number of inversions.



def merge(A,B,C):
    i,j,k = 0,0,0
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i]
            i +=1
        else: 
            A[k] = C[j]
            j+=1
        k +=1

    if i < len(B):
        A[k:] = B[i:]
    if j < len(C):
        A[k:] = B[j:]


def MergeSort(A):
    
    if(len(A) > 1):
        mid = len(A)//2
        B =  A[:mid]
        C = A[mid:]    
        MergeSort(B)
        MergeSort(C)
        merge(A,B,C)


b = [4,3,2,1,0]

print(b)

MergeSort(b)

print(b)
