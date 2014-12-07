# -*- coding: utf-8 -*-
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

@author: n609874
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers

## 1. first transpose, then
## clockwise: reflect with mid col; anticlockwise: reflect with mid row
## O(mn), but two runs
#    def rotate(self, matrix):
#        if not matrix: return matrix
#    
#        n = len(matrix)
#        for i in xrange(n):
#            for j in xrange(i + 1, n):
#                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#                
#        for j in xrange(n/2):
#            for i in xrange(row):
#                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
#        return matrix

## 2. in Python, we can simplify the reflection by reverse
#    def rotate(self, matrix):
#        if not matrix: return matrix                
#        n = len(matrix)
#        for i in xrange(n):
#            for j in xrange(i + 1, n):
#                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]                
#            matrix[i].reverse()
#        
#        return matrix

# 3. O(mn), but one run
    def rotate(self, matrix):
        if not matrix: return matrix
        
        n = len(matrix)
        for i in xrange(n/2):
            for j in xrange(i, n - 1 - i):
                temp = matrix[i][j]
                matrix[i][j] =  matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]                
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp
    
        return matrix
    
if __name__ == "__main__":
    test = Solution()
    matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    print test.rotate(matrix)