def main():
    print(check_for_winner([[1, 2, 0], [2, 1, 0], [2, 1, 1]]))  # diagonal winner = 1
    print(check_for_winner([[1, 2, 1], [2, 2, 0], [1, 2, 1]]))  # column winner = 2
    print(check_for_winner([[1, 2, 0], [2, 1, 2], [1, 1, 1]]))  # row winner = 1
    print(check_for_winner([[1, 2, 0], [2, 0, 0], [2, 1, 2]]))  # no winner = 0

def check_rows(board):
    for row in board:
        if row[0] != 0 and row[0] == row[1] == row[2]:
            return row[0]
    return 0

def check_columns(board):
    for i in range(3):
        if board[0][i] != 0 and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        
    return 0

def check_diagonals(board):
    if board[1][1] == 0:
        return 0
    
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    
    if board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return 0

def check_for_winner(board):
    return check_rows(board) or check_columns(board) or check_diagonals(board)


if __name__ == "__main__":
    main()