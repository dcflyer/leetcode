# -*- coding: utf-8 -*-
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

@author: Dennis
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if not A: return 0
        
        last, curr, step = 0, 0, 0
        for i in xrange(len(A)):
            if i > last:
                last = curr
                step += 1
            curr = max(curr, i + A[i])
        
        if curr >= len(A) - 1:
            return step
        else:
            return 0
        
if __name__ == "__main__":
    test = Solution()
    print test.jump([2,3,1,1,4])
        
        