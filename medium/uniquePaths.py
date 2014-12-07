# -*- coding: utf-8 -*-
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

@author: n609874
"""
class Solution:
    # @return an integer
# 1. use DP
    def uniquePaths(self, m, n):
        if m < 1 or n < 1: return 0
        if m == 1 or n == 1: return 1
        
        res = [0]*n
        res[0] = 1
        
        for i in xrange(m):
            for j in xrange(1, n):
                res[j] += res[j - 1]
        
        return res[n - 1]
# 2. use combination C_{m + n - 2}^{m - 1}, check integer overflow 
#    def uniquePaths(self, m, n):
#        if m < 1 or n < 1: return 0
#        if m == 1 or n == 1: return 1
#        
#        small = m - 1 if m < n else n - 1
#        large = m - 1 if m > n else n - 1 
#        num, dem = 1, 1
#        for i in xrange(small):
#            num *= large + small - i
#            dem *= small - i
#        
#        return num/dem
        
if __name__ == "__main__":
    test = Solution()
    print test.uniquePaths(3,3)
        
        
        
