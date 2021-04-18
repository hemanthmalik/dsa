def initialize_board(n):
    board = {i: {} for i in ['queen', 'row', 'col', 'nwtose', 'swtone']}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1), n):
        board['nwtose'][i] = 0
    for i in range(2*n-1):
        board['swtone'][i] = 0
    return board

def printboard(board):
    for row in sorted(board['queen'].keys()):
        print(row, board['queen'][row])

def free(i, j, board):
    return board['row'][i] == board['col'][j] == board['nwtose'][j-i] == board['swtone'][j+i] == 0

def addqueen(i, j, board):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['nwtose'][j-i] = 1
    board['swtone'][j+i] = 1

def undoqueen(i, j, board):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][j-i] = 0
    board['swtone'][j+i] = 0

def placequeen(n, i, board):
    for j in range(n):
        if free(i, j, board):
            addqueen(i,j,board)
            if i==n-1:
                return True
            else:
                extendsoln = placequeen(n, i+1, board)
            if extendsoln:
                return True
            else:
                undoqueen(i, j, board)
    else:
        return False

    
n = int(input("Enter number of queens: "))
board = initialize_board(n)
if placequeen(n, 0, board):
    printboard(board)