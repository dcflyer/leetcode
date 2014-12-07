# -*- coding: utf-8 -*-
"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. 
Only the filled cells need to be validated. 

@author: weichen
"""
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean

# 1. time complexity O(n^2), space complexity O(n^2)
    def isValidSudoku(self, board):

        l = [False]*9
        rows = [l[:] for x in xrange(9)]
        columns = [l[:] for x in xrange(9)]
        blocks = [l[:] for x in xrange(9)]
        
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == ".": continue
                c = int(board[i][j]) - 1
                if rows[i][c] or columns[j][c] or blocks[i - i%3 + j/3][c]:
                    return False
                else:
                    rows[i][c] = True
                    columns[j][c] = True
                    blocks[i - i%3 + j/3][c] = True
        return True

if __name__ == "__main__":
    test = Solution()
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print test.isValidSudoku(board)                
                        