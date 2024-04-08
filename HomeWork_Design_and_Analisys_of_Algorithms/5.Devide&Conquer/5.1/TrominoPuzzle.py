def Tromino(board, size, hole, tile=1, row=None, col=None):
    if row is None:
        row = (0, size - 1)
    if col is None:
        col = (0, size - 1)

    if size == 2:
        for i in range(row[0], row[1] + 1):
            for j in range(col[0], col[1] + 1):
                if board[i][j] == 0:
                    board[i][j] = tile
        return tile + 1
    
    row_mid = (row[1] + row[0]) // 2
    col_mid = (col[1] + col[0]) // 2
    newHole = [(row_mid, col_mid), (row_mid, col_mid + 1), (row_mid + 1, col_mid), (row_mid + 1, col_mid + 1)]
    
    hole_locate_in_Quandrant = 1
    if hole[0] <= row_mid:
        if hole[1] > col_mid:
            hole_locate_in_Quandrant = 2
    else: 
        if hole[1] <= col_mid:
            hole_locate_in_Quandrant = 3
        else: 
            hole_locate_in_Quandrant = 4
           
    sm = [((row[0], row_mid), (col[0], col_mid)),  # gocphantu 1
          ((row[0], row_mid), (col_mid + 1, col[1])),  # gocphantu 2
          ((row_mid + 1, row[1]), (col[0], col_mid)),  # gocphantu 3
          ((row_mid + 1, row[1]), (col_mid + 1, col[1]))]  # gocphantu 4
    contain = [False] * 4  # check coi góc phần tư da vào
    contain[hole_locate_in_Quandrant - 1] = True
    for i, (hole_row, hole_col) in enumerate(newHole):
        if not contain[i]:
            board[hole_row][hole_col] = tile 
    tile = tile +1       
    

    
    for i, (hole_row, hole_col) in enumerate(newHole):
        if not contain[i]:
            contain[i] = True
            tile = Tromino(board, size // 2, (hole_row, hole_col), tile , sm[i][0], sm[i][1])
        else:
            tile = Tromino(board, size // 2, hole, tile , sm[i][0], sm[i][1])

    return tile 

hole = (1, 1)

n = 6
size = 2 ** n
board = [[0] * size for _ in range(size)]
board[hole[0]][hole[1]] = -1
Tromino(board, size, hole)
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
print_matrix(board)
# matrix_np = np.array(matrix_data)
# # Make the matrix symmetric
# symmetric_matrix = (matrix_np + matrix_np.T) / 2

# # Print out the symmetric matrix
# for row in symmetric_matrix:
#     print(' '.join(map(lambda x: f'{x:.0f}'.rjust(3), row)))