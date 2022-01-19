import math

class SudokuSolver():
    ''' A simple sudoku solver using a backtracking algorithim'''
    def __init__(self):
        self.boardSize=9 #Shouldn't be changed since sudoku standard is a 3x3 grid anyways
        self.board=[
            [0,8,0,0,0,9,7,4,3],
            [0,5,0,0,0,8,0,1,0],
            [0,1,0,0,0,0,0,0,0],
            [8,0,0,0,0,5,0,0,0],
            [0,0,0,8,0,4,0,0,0],
            [0,0,0,3,0,0,0,0,6],
            [0,0,0,0,0,0,0,7,0],
            [0,3,0,5,0,0,0,8,0],
            [9,7,2,4,0,0,0,5,0]] #0 indicates a blank space on the sudoku board   
                
        
        if (self.run(self.board,0,0)):
            self.printer(self.board)
        else:
            print("A solution does not exist for this board\n" + self.board)
        
    def printer(self, x):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if (i==3 and j==0 or i==6 and j==0):
                    print("---------------------",end="\n")
                if (j==3 or j==6):
                    print("|",end=" ")
                print(x[i][j],end= " ")
            print()
    
    def solve(self, board, row, col, num):
        for i in range(self.boardSize):
            if self.board[row][i]==num:
                return False
            
        for j in range(self.boardSize):
            if self.board[j][col]==num:
                return False
        
        rowStart= row-row % 3
        colStart= col-col % 3
        
        '''Taking the board size and making it into smaller grids
        Then we check to see if there is already the same number in our smaller grids'''
        
        for k in range(3): 
            for l in range(3):
                if board[k+rowStart][l+colStart] == num:
                    return False
        return True

    def run(self, board, row, col):
        
        if (row == self.boardSize - 1 and col == self.boardSize):
            return True
        if col == self.boardSize:
            row += 1
            col = 0
        if self.board[row][col] > 0:
            return self.run(self.board, row, col + 1)
        for num in range(1, self.boardSize + 1, 1): 
            if self.solve(self.board, row, col, num):
                self.board[row][col] = num
                if self.run(self.board, row, col + 1):
                    return True
            self.board[row][col] = 0 #Essentially the 'reset' if we need to start over
        return False

if __name__ == '__main__':
    SudokuSolver()
