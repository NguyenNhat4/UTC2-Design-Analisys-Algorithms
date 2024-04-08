def matrix_addition(A, B):
    
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same size")
    
    result = [[0 for col in range(len(A[0]))] for row in range(len(A))]
    
    for row in range(len(A)):
        for col in range(len(A[0])):
            result[row][col] = A[row][col] + B[row][col]
    return result

def matrix_subtraction(A, B):
    
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same size")
    
    result = [[0 for col in range(len(A[0]))] for row in range(len(A))]
    
    for row in range(len(A)):
        for col in range(len(A[0])):
            result[row][col] = A[row][col] - B[row][col]
    return result

def strassen(a, b):
    if len(a) == 1 and len(a[0]) == 1:
        return a[0][0] * b[0][0]
    else:
        
        quad1_a, quad2_a, quad3_a, quad4_a = divide(a)
        quad1_b, quad2_b, quad3_b, quad4_b = divide(b)

        
        p1 = strassen(matrix_addition(quad1_a, quad4_a), matrix_addition(quad1_b, quad4_b))
        p2 = strassen(matrix_addition(quad3_a, quad4_a), quad1_b)
        p3 = strassen(quad1_a, matrix_subtraction(quad3_b, quad1_b))
        p4 = strassen(quad4_a, matrix_subtraction(quad3_b, quad1_b))
        p5 = strassen(matrix_addition(quad1_a, quad2_a), quad4_b)
        p6 = strassen(matrix_subtraction(quad3_a, quad1_a), matrix_addition(quad1_b, quad2_b))
        p7 = strassen(matrix_subtraction(quad2_a, quad4_a), matrix_addition(quad3_b, quad4_b))

        
        final_quad1 = matrix_subtraction(matrix_addition(p1, p4), matrix_addition(p5, p7))
        final_quad2 = matrix_addition(p3, p5)
        final_quad3 = matrix_addition(p2, p4)
        final_quad4 = matrix_addition(matrix_subtraction(p1, p2), matrix_addition(p3, p6))
        resultant_matrix = combine_submatrices(final_quad1, final_quad2, final_quad3, final_quad4)
        return resultant_matrix


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]
result = strassen(A, B)
print(result)

