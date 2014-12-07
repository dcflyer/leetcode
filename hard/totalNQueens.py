# -*- coding: utf-8 -*-
"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
@author: weichen
"""

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.n = n
        self.res = 0
        rowColumns = [-1 for x in xrange(n)]
        self.nQueens(0, rowColumns)
        return self.res
        
    def nQueens(self, row, rowColumns):
        if row == self.n: 
            self.res += 1
        else:        
            for i in xrange(self.n):
                rowColumns[row] = i
                if self.checkValid(row, rowColumns):
                    self.nQueens(row + 1, rowColumns)
    
    def checkValid(self, row, rowColumns):
        for i in xrange(0, row):
            if rowColumns[i] == rowColumns[row] or \
                abs(rowColumns[i] - rowColumns[row]) == row - i:
                return False
        return True

if __name__ == "__main__":
    test = Solution()
    res = test.totalNQueens(4)
    print res            
    