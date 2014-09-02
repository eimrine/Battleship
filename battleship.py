from random import randint

arrMainBoard = []
arrPrevBoard = []
arrShipBoard = []
intBoardSize = 5
intBoatsNum = 4
intWinCond = 4 #need 4 decrements to win
ship1 = [-1,-1]
ship2 = [-1,-1]
ship3 = [-1,-1]
ship4 = [-1,-1]

# Main board init
for x in range(intBoardSize):
    arrMainBoard.append(["U"] * intBoardSize)
    
# Prev board init
for x in range(intBoardSize):
    arrPrevBoard.append([False] * intBoardSize)
    
# Ship board init
for x in range(intBoardSize):
    arrShipBoard.append([False] * intBoardSize)    

def print_board(arrMainBoard):
    for row in arrMainBoard:
        print " ".join(str(row))

print "Let's play Battleship!"
print_board(arrMainBoard)

    


# CPU turn
def random_row(arrMainBoard):
    return randint(0, len(arrMainBoard) - 1)

def random_col(board):
    return randint(0, len(arrMainBoard[0]) - 1)

def lstRandomPair():
    result = []
    x = randint(0, len(arrMainBoard) - 1)
    y = randint(0, len(arrMainBoard[0]) - 1)
    result = [x,y]
    return result

def shipPlacing():
    #TODO:  locate on this map pls
    result = []
    while (True):
        pair = lstRandomPair()
        if prevent(pair) == False:
            arrPrevBoard[pair[0]][pair[1]] = True
            arrShipBoard[pair[0]][pair[1]] = True
            break
        return pair

def seek(input):
    if (input[0] < 0 or input[0] >= intBoardSize) or (input[1] < 0 or input[1] >= intBoardSize):
        print "Oops, that's not even in the ocean."
        return False
    else:
        return True

def shot(input):
    if (arrShipBoard[input[0]][input[1]] == False):
        return False
    else:     
        return True    
    
def prevent(input):
    if (arrPrevBoard[input[0]][input[1]] == False):
        return False
    else:     
        return True

for i in range(intBoatsNum):
    shipPlacing()


    
# Prev board print
print "arrPrevBoard START"
print_board(arrPrevBoard)
print "arrPrevBoard END" 

print "arrShipBoard START"
print_board(arrShipBoard)
print "arrShipBoard END"     
        
for turn in range(4):
    if intWinCond == 0:
        print "Congratulations, you are the winner! Quitting."
    print "Your turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    output = []
    output = [guess_row, guess_col]
    if shot(output) == True:
        print "additional turn!"
        turn += 1
    else:
        if (seek(output) == False ): 
            print "turn is not counted"
        elif(arrMainBoard[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            arrMainBoard[guess_row][guess_col] = "X"
        print (turn + 1)
        print_board(arrMainBoard)
    if turn == 3:
        print "Game Over"
