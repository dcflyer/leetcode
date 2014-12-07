# -*- coding: utf-8 -*-
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

@author: n609874
"""
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0
        for x in A:
            one ^= x
        return one
        
#    def singleNumber(self, A):
#        if not A: return -1
#        one = A[0]
#        for i in xrange(1, len(A)):
#            one = one ^ A[i]
#        return one
        
if __name__ == "__main__":
    test = Solution()
    print test.singleNumber([-2,-1,-3,2,-3,-1,-2])
