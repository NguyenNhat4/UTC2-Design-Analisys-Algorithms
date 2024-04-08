# Let A[0..n − 1] be an array of n real numbers. A pair (A[i], A[j ]) is said to
# be an inversion if these numbers are out of order, i.e., i < j but A[i] > A[j ].
# Design an O(n log n) algorithm for counting the number of inversions.



def MergeCount(A,B,C):
    count = 0
    i,j,k = 0,0,0
    sizeB, sizeC = len(B), len(C)

    while i < sizeB and j < sizeC:
        if B[i] > C[j]:
            A[k] = B[i]
            count += (sizeC-j)
            
            i +=1
        else: 
            A[k] = C[j]
           
            j+=1
        k +=1

    if i < sizeB:
        A[k:] = B[i:]
       
    if j < sizeC:
        A[k:] = B[j:]
    return count

def MergeSortAndCountInverse(A):
    
    if(len(A) > 1):
        mid = len(A)//2
        B =  A[:mid]
        C = A[mid:]    
     
       
        l=MergeSortAndCountInverse(B)
        r= MergeSortAndCountInverse(C)
        res = MergeCount(A,B,C)


        return res + l + r    
    else: 
        return 0


b = [4,3,2,1,0]

print("res :",MergeSortAndCountInverse(b))
