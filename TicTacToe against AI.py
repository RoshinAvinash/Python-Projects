import time
board = [ x for x in range(10)]

def printBoard(board):
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))
    print('-----------')
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
    print('-----------')
    print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9]))

#for inserting X or O on the board
def LetterInsert(letter, pos):  
    board[pos] = letter


#For checking if there is space in any particular position
def spaceIsFree(pos):   
    return board[pos] == pos

#Conditions for winning the game  
def WinnerCondition(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    LetterInsert('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def ComputerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == 1 or letter ==2 or letter==3 or letter==4 or letter==5 or letter ==6 or letter ==7 or letter ==8 or letter ==9 and x != 0]
    move = 0
    time.sleep(0.5)  #For delaying the computer move by 0.5 seconds

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if WinnerCondition(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move


#Condition to check if board is full or not
def isBoardFull(board):
    if (board.count("X") + board.count("O")) !=9:
        return False
    else:
        return True

def play():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(WinnerCondition(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(WinnerCondition(board, 'X')):
            move = ComputerMove()
            if move == 0:
                print('Tie Game!')
            else:
                LetterInsert('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [ x for x in range(10)]
        print('-----------------------------------')
        play()
    else:
        print("Thanks for playing, Hope to see you again")
        break