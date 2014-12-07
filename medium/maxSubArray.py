# -*- coding: utf-8 -*-
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum. 

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6. 

More practice: 
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

@author: n609874
"""
class Solution:
    # @param A, a list of integers
    # @return an integer

## NOT GOOD, only works for nonegative maxSum
#    def maxSubArray(self, A):
#        if not A: return 0
#        
#        maxSum = -10000
#        curr = 0
#        for i in A:
#            if curr + i > 0:
#                curr = curr + i
#            else:
#                curr = 0
#            maxSum = max(maxSum, curr)
#        
#        return maxSum
        
    def maxSubArray(self, A): 
        if not A: return 0
        
        curr = A[0]; maxSum = A[0]
        for i in xrange(1, len(A)):
            curr = max(A[i], curr + A[i])
            maxSum = max(maxSum, curr)
        
#        if maxSum < 0: return 0
        return maxSum

if __name__ == "__main__":
    test = Solution()
    print test.maxSubArray([-2,-1,-1,-3])
    
