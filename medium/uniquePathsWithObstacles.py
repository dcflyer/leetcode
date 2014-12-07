# -*- coding: utf-8 -*-
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,


There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

@author: n609874
"""
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        res = [0]*n; res[0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    res[j] = 0
                else:
                    if j > 0: res[j] += res[j - 1]
        
        return res[n - 1]
        
if __name__ == "__main__":
    test = Solution()
    l = [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    print test.uniquePathsWithObstacles(l)

        
        
        
        
