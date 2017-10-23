def is_solved(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 0
    else:
        return -1
    

if __name__ == '__main__':
    
    board = [[0] * 3 for _ in range(3)] 
    
    for i in range(3):
        for j in range(3):
            board[i][j] = int(input()) 
    
    print(is_solved(board))
