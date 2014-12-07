# -*- coding: utf-8 -*-
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

@author: n609874
"""

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid: return 0
                
        m, n = len(grid), len(grid[0])
        res = [0]*n
#        WRONG !!! first row should be handled differently
#        Don't forget the following three lines
        res[0] = grid[0][0]
        for j in xrange(1, n):
            res[j] = res[j - 1] + grid[0][j]
        
        for i in xrange(1, m):
            for j in xrange(n):
                if 0 == j:
                    res[j] += grid[i][j]
                else:
                    res[j] = min(res[j - 1], res[j]) + grid[i][j]
        
        return res[n - 1]
        
if __name__ == "__main__":
    test = Solution()
    l = [[1,3,1],[1,5,1],[4,2,1]]
    print test.minPathSum(l)
        
        
        
        
        