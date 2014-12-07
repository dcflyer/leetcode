# -*- coding: utf-8 -*-
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution. 

@author: weichen
"""
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solveEntry(board, 0, 0)
        
    def solveEntry(self, board, row, col):
        if row == 9: return True
        if col == 9:
            return self.solveEntry(board, row + 1, 0)
        if board[row][col] != '.':
            return self.solveEntry(board, row, col + 1)
        for i in xrange(1, 10):
            if self.isValid(board, str(i), row, col):
                board[row][col] = str(i)
                if self.solveEntry(board, row, col + 1):
                    return True
                board[row][col] = "."
        return False
        
    def isValid(self, board, char, row, col):
        for k in xrange(9):
            if board[row][k] == char: return False
            if board[k][col] == char: return False
        for i in xrange(row//3*3, row//3*3 + 3):
            for j in xrange(col//3*3, col//3*3 + 3):
                if board[i][j] == char:
                    return False
        return True
        
if __name__ == "__main__":
    test = Solution()
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print test.solveSudoku(board)         
            
