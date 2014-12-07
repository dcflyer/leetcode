# -*- coding: utf-8 -*-
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 

@author: weichen
"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A: return -1
        
        max_local, min_local, max_global = A[0], A[0], A[0]
        for i in xrange(1, len(A)):
            max_copy = max_local
            max_local = max(max_copy*A[i], min_local*A[i], A[i])
            min_local = min(max_copy*A[i], min_local*A[i], A[i])
            if max_local > max_global:
                max_global = max_local
        
        return max_global

if __name__ == "__main__":
    test = Solution()
    print test.maxProduct([-1,3,-4,2,2,2,-1])
            


