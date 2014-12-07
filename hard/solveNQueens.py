# -*- coding: utf-8 -*-
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

@author: weichen
"""
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
######        Can define field in a member function
        self.n = n
        res = []
        rowColumns = [-1 for x in xrange(n)]
        self.nQueens(0, rowColumns, res)
        return res
        
    def nQueens(self, row, rowColumns, res):
        if row == self.n:
            res.append(self.createPuzzle(rowColumns))
        else:
            for i in xrange(self.n):
                rowColumns[row] = i
                if self.checkValid(rowColumns, row):
                    self.nQueens(row + 1, rowColumns, res)
        
    def checkValid(self, rowColumns, row):
        for i in xrange(0, row):
            if rowColumns[i] == rowColumns[row] or \
                abs(rowColumns[i] - rowColumns[row]) == row - i:
                return False
        return True
    
    def createPuzzle(self, rowColumns):
        puzzle = []
        row = ['.' for x in xrange(self.n)]
        for i in xrange(self.n):
            newrow = row[:]
            newrow[rowColumns[i]] = 'Q'
#            puzzle.append(newrow)
            puzzle.append(''.join(newrow))
        return puzzle
        
if __name__ == "__main__":
    test = Solution()
    res = test.solveNQueens(5)
    print res
                
            