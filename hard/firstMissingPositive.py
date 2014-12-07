# -*- coding: utf-8 -*-
"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

@author: Dennis
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A: return 1
        
        i = 0
        
#        WRONG !!! i -= 1 cannot change i in xrange
#        for i in xrange(len(A)):
        while i < len(A): 
#            WRONG !!! we update A[i] first, then use A[i] in A[A[i] - 1]
#            if A[i] != i + 1 and A[i] > 0 and A[i] < len(A) and A[A[i] - 1] != A[i]:
#                temp = A[i]
#                A[i] = A[A[i] - 1]
#                A[A[i] - 1] = temp
        
            if A[i] > 0 and A[i] < len(A) and A[i] != A[A[i] - 1]:
                temp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = temp
#                WRONG!!! need to go back
                i -= 1
            i += 1
        
        for i in xrange(len(A)):
            if A[i] != i + 1:
                return i + 1
        
        return len(A) + 1
                
if __name__ == "__main__":
    test = Solution()
    print test.firstMissingPositive([-1,4,2,1,9,10])