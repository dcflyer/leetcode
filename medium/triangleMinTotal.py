# -*- coding: utf-8 -*-
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

@author: Dennis
"""
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer

## not good enough (Time Limit Exceeded)
#    def minimumTotal(self, triangle):
#        if not triangle: return -1
#        self.n = len(triangle)
#        self.res = sum([sum(x) for x in triangle])
#        path = []
#        self.pathSum(path, 0, 0, triangle)
#        return self.res
#            
#        
#    def pathSum(self, path, row, col, triangle):
##        WRONG !!! once row = self.n, should definitly return
##        if row == self.n and sum(path) < self.res:
##            self.res = sum(path)
#        if row == self.n:
#            if sum(path) < self.res:
#                self.res = sum(path)
#            return
#        
#        path.append(triangle[row][col])
#        self.pathSum(path[:], row + 1, col, triangle)
#        path.pop()
#        if row > 0:
#            path.append(triangle[row][col + 1])
#            self.pathSum(path[:], row + 1, col + 1, triangle)

#    def minimumTotal(self, triangle):
#        if not triangle: return -1
#        if len(triangle) == 1: return triangle[0][0]        
#        triangle = triangle[:]
#        level = len(triangle)
#        
#        minPath = triangle[0][0]            # not good enough
#        for i in xrange(1, level):
#            minPath += triangle[i][i]       # add first before triangle changed
#            for j in xrange(i+1):
#                if j == 0:
#                    triangle[i][j] += triangle[i - 1][j]
#                elif j == len(triangle[i]) - 1:
#                    triangle[i][j] += triangle[i - 1][j - 1]
#                else:
#                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
#            
#        
#        for j in xrange(level):
#            if triangle[level-1][j] < minPath:
#                minPath = triangle[level-1][j]
#        
#        return minPath
        
    def minimumTotal(self, triangle):
        if not triangle: return -1
        
        n = len(triangle)
        minPath = [0]*len(triangle[n - 1])
        for i in xrange(n - 1, -1, -1):
            for j in xrange(i + 1):
                if i == n - 1:
                    minPath[j] = triangle[i][j]
                else:
                    minPath[j] = min(minPath[j], minPath[j + 1]) + triangle[i][j]
        return minPath[0]     
        
    
if __name__ == "__main__":
    test = Solution()
#    l = [
#         [2],
#        [3,4],
#       [6,5,7],
#      [4,1,8,3]
#      ]
      
    l = [[-1],[-2,-3]]
    print test.minimumTotal(l)