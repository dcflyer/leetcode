# -*- coding: utf-8 -*-
"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3, 

You should return the following matrix: 
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

@author: n609874
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n <= 0: return []
            
        res = [[0 for i in xrange(n)] for j in xrange(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        direct, curr = 0, 0
        
        while True:
            if 0 == direct:     # go right
                for i in xrange(left, right + 1):
                    curr += 1; res[top][i] = curr
                top += 1
            elif 1 == direct:   # go down
                for i in xrange(top, bottom + 1):
                    curr += 1; res[i][right] = curr
                right -= 1
            elif 2 == direct:
                for i in reversed(xrange(left, right + 1)):
                    curr += 1; res[bottom][i] = curr
                bottom -= 1
            else:
                for i in reversed(xrange(top, bottom + 1)):
                    curr += 1; res[i][left] = curr
                left += 1
            if top > bottom or left > right: return res
            direct = (direct + 1)%4            

if __name__ == "__main__":
    test = Solution()
    print test.generateMatrix(3)        