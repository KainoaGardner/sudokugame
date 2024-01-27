def solve(board,r=0,c=0):
    if r == 9:
        return True
    elif c == 9:
        return solve(board,r+1,0)
    elif board[r][c] != 0:
        return solve(board,r,c+1)
    else:
        for n in range(1,10):
            if isValid(board,r,c,n):
                board[r][c] = n
                if solve(board,r,c+1):
                    return True
                board[r][c] = 0
        return False

def isValid(board,r,c,n):
    notInRow = n not in board[r]
    notInCol = n not in [board[i][c] for i in range(9)]
    notInBox = n not in [board[i][j] for i in range(r//3*3,r//3*3 + 3) for j in range(c//3*3,c//3*3 +3)]
    return notInRow and notInCol and notInBox