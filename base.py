#file = open("output.txt","w")

# function to print the board on to a file.
# returns a string variable with the board info


# function to print the board on to the console
def printBoard(board):
    print(board)
    
    
# function to check if the board is full or not
# returns true if it is full and false if it isn't
# it works on the fact that if it finds at least one 
# zero in the board it returns false
def isFull(board):
    for x in range(0, 5):
        for y in range (0, 5):
            if board[x][y] == 0:
                return False
    return True
    
# function to find all of the possible numbers
# which can be put at the specifies location by
# checking the horizontal and vertical and the 
# three by three square in which the numbers are
# housed
def possibleEntries(board, i, j):
    
    possibilityArray = {}
    
    for x in range (1, 6):
        possibilityArray[x] = 0
    
    #For horizontal entries
    for y in range (0, 5):
        if not board[i][y] == 0: 
            possibilityArray[board[i][y]] = 1
     
    #For vertical entries
    for x in range (0, 5):
        if not board[x][j] == 0: 
            possibilityArray[board[x][j]] = 1
            
       
    
    for x in range (1, 6):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray

# recursive function which solved the board and 
# prints it. 
def sudokuSolver(board):
    
    i = 0
    j = 0
    
    possiblities = {}
    
    # if board is full, there is no need to solve it any further
    if isFull(board):
        print("Board Solved Successfully!")
        printBoard(board)
        return True
    else:
        # find the first vacant spot
        for x in range (0, 5):
            for y in range (0, 5):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
        # get all the possibilities for i,j
        possiblities = possibleEntries(board, i, j)
        
        # go through all the possibilities and call the the function
        # again and again
        for x in range (1, 6):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]
                #file.write(printFileBoard(board))
                print(x)
                if sudokuSolver(board)==True:
                    break
                else:
                    sudokuSolver(board)
        # backtrack
        board[i][j] = 0

def main():
    SudokuBoard = [[0 for x in range(5)] for x in range(5)] 
    SudokuBoard[0][0] = 0
    SudokuBoard[0][1] = 0
    SudokuBoard[0][2] = 0
    SudokuBoard[0][3] = 0
    SudokuBoard[0][4] = 0
   
    SudokuBoard[1][0] = 0
    SudokuBoard[1][1] = 0
    SudokuBoard[1][2] = 0
    SudokuBoard[1][3] = 0
    SudokuBoard[1][4] = 0

    SudokuBoard[2][0] = 0
    SudokuBoard[2][1] = 0
    SudokuBoard[2][2] = 0
    SudokuBoard[2][3] = 0
    SudokuBoard[2][4] = 0

    SudokuBoard[3][0] = 0
    SudokuBoard[3][1] = 0
    SudokuBoard[3][2] = 0
    SudokuBoard[3][3] = 0
    SudokuBoard[3][4] = 0

    SudokuBoard[4][0] = 0
    SudokuBoard[4][1] = 0
    SudokuBoard[4][2] = 0
    SudokuBoard[4][3] = 0
    SudokuBoard[4][4] = 0


    #printBoard(SudokuBoard)
    sudokuSolver(SudokuBoard)
    #file.close()
    
if __name__ == "__main__":
    main()
