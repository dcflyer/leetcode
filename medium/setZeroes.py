# -*- coding: utf-8 -*-
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place. 

click to show follow up.
Follow up: 
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution? 

@author: n609874
"""

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.

## 1. use O(m + n) space, not good enough
#    def setZeroes(self, matrix):
#        if not matrix: return 
#        
#        rowZeros, colZeros = [], []
#        for i in xrange(len(matrix)):
#            for j in xrange(len(matrix[i])):
#                if 0 == matrix[i][j]:
#                    rowZeros.append(i); colZeros.append(j)
#        
#        for i in rowZeros:
#            for j in xrange(len(matrix[i])):
#                matrix[i][j] = 0
#        for j in colZeros:
#            for i in xrange(len(matrix)):
#                matrix[i][j] = 0

# 2. O(1) space
    def setZeroes(self, matrix):
        if not matrix: return
        
        rowFlag, colFlag = False, False
        for j in xrange(len(matrix[0])):
            if 0 == matrix[0][j]:
                rowFlag = True; break
            
        for i in xrange(len(matrix)):
            if 0 == matrix[i][0]:
                colFlag = True; break
        
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[i])):
                if 0 == matrix[i][j]:
                    matrix[i][0] = 0; matrix[0][j] = 0
        
        for j in xrange(1, len(matrix[0])):
            if 0 == matrix[0][j]:
                for k in xrange(1, len(matrix)):
                    matrix[k][j] = 0
        for i in xrange(1, len(matrix)):
            if 0 == matrix[i][0]:
                for k in xrange(1, len(matrix[i])):
                    matrix[i][k] = 0
                    
        if rowFlag:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0
        if colFlag:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0
           

if __name__ == "__main__":
    test = Solution()
    matrix = [[1,2,3,4],[2,0,1,0]]
    test.setZeroes(matrix)
    print matrix