# -*- coding: utf-8 -*-
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

@author: weichen
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

#    def search(self, A, target):
#        if not A: return -1
#        
#        l = 0; r = len(A) - 1
#        
#        while l <= r:
#            m = (l + r)//2
#            if A[m] == target:
#                return m
##            WRONG !!! don't work for [2,1], 1. 
##            for reason, please check findMinI
##            elif A[l] < A[m]:                
#            elif A[l] <= A[m]:
#                if A[l] <= target and target < A[m]:
#                    r = m - 1
#                else:
#                    l = m + 1
#            else:
#                if A[m] < target and target <= A[r]:
#                    l = m + 1
#                else:
#                    r = m - 1
#        return -1
    def search(self, A, target):
        if not A: return -1
        
        l = 0; r = len(A) - 1
        
        while l <= r:
            m = (l + r)//2
            if A[m] == target:
                return m
            elif A[m] < A[r]:
                if A[m] < target and target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if A[l] <= target and target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

if __name__ == "__main__":
    test = Solution()
#    A = [4, 5, 6, 7, 0, 1, 2]
    A = [2,1]

    target = 1
    print test.search(A, target)
                
    