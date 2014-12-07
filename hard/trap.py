# -*- coding: utf-8 -*-
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

@author: Dennis
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
# 1. one time run
    def trap(self, A):
        if not A: return 0

        l, r = 0, len(A) - 1
        res = 0
        while l < r:
            minbar = min(A[l], A[r])
            if A[l] == minbar:
                l += 1
                while l < r and A[l] < minbar:
                    res += minbar - A[l]
                    l += 1
            else:
                r -= 1
                while l < r and A[r] < minbar:
                    res += minbar - A[r]
                    r -= 1
        
        return res
        
## 2. two times run
#    def trap(self, A):
#        if not A: return 0
#        container = [0]*len(A)
#        res = 0
#        
#        maxbar = 0
#        for i in xrange(len(A)):
#            container[i] = maxbar
#            maxbar = max(A[i], maxbar)
#            
#        maxbar = 0
#        for i in xrange(len(A) - 1, -1, -1):
#            container[i] = min(maxbar, container[i])
#            res += max(container[i] - A[i], 0)
#            maxbar = max(A[i], maxbar)
#            
#        return res
                
if __name__ == "__main__":
    test = Solution()
    print test.trap([0,1,0,2,1,0,1,3,2,1,2,1])
                
        