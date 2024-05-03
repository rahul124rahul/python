
# N Queen Problem 

N = int(input("Enter the number of queens : "))

board = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(0)
    board.append(row)


def is_attack(i, j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False


def N_queen(n):
    if n==0:
        return True
    for i in range(N):
        for j in range(N):
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0
    return False


N_queen(N)
for row in board:
    for cell in row:
        if cell == 1:
            print('Q', end=' ')
        else:
            print('-', end=' ')
    print()