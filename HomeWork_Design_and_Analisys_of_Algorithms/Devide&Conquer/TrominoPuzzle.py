def tromino(board, size, hole, tile=1):
    # Base case: if the board size is 2x2, place the tromino
    if size == 2:
        for i in range(2):
            for j in range(2):
                if board[hole[0] // size * 2 + i][hole[1] // size * 2 + j] == 0:
                    board[hole[0] // size * 2 + i][hole[1] // size * 2 + j] = tile
        return  1

    # Recursive case: divide the board into four quadrants
    half = size // 2
    centers = [(half - 1, half - 1), (half - 1, half), (half, half - 1), (half, half)]
    for i, (dx, dy) in enumerate(centers):
        if hole[0] < half and hole[1] < half:  
            new_hole = hole if i == 0 else (dx, dy)
        elif hole[0] < half and hole[1] >= half:  
            new_hole = hole if i == 1 else (dx, dy)
        elif hole[0] >= half and hole[1] < half: 
            new_hole = hole if i == 2 else (dx, dy)
        else:  
            new_hole = hole if i == 3 else (dx, dy)

        # Adjust the hole position for the next level
        if i > 0:
            new_hole = (new_hole[0] % half, new_hole[1] % half)

        # Recursively solve for the next quadrant
        tile = tromino(board, half, new_hole, tile)

    # Place the tromino in the center
    board[centers[0][0]][centers[0][1]] = board[centers[1][0]][centers[1][1]] = \
        board[centers[2][0]][centers[2][1]] = board[centers[3][0]][centers[3][1]] = tile

    return  1

# Example usage
n = 4  # Size of the board (2^n x 2^n)
board = [[0 for _ in range(n)] for _ in range(n)]
hole = (1, 1)  # Position of the missing square
tromino(board, n, hole)

# Print the board
for row in board:
    print(' '.join(str(x) for x in row))
