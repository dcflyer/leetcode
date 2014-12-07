# -*- coding: utf-8 -*-
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order. 

For example,
Given the following matrix: 

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]. 

@author: n609874
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        if not matrix: return res
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        direct = 0
        
        while True:
            if 0 == direct:     # go right
                for i in xrange(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            elif 1 == direct:   # go down
                for i in xrange(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif 2 == direct:
                for i in reversed(xrange(left, right + 1)):
                    res.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in reversed(xrange(top, bottom + 1)):
                    res.append(matrix[i][left])
                left += 1
            if top > bottom or left > right: return res
            direct = (direct + 1)%4
            
if __name__ == "__main__":
    test = Solution()
    matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    print test.spiralOrder(matrix)            