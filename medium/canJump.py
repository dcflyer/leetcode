# -*- coding: utf-8 -*-
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

@author: Dennis
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if not A: return False
        
        reach = 0
        for i in xrange(len(A)):
            if i <= reach:
                reach = max(reach, i + A[i])
        
        return True if reach >= len(A) - 1 else False
        
if __name__ == "__main__":
    test = Solution()
    print test.canJump([2,3,1,1,4])
    print test.canJump([3,2,1,0,4])
        