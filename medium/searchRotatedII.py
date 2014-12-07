# -*- coding: utf-8 -*-
"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

@author: weichen
"""

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if not A: return False
    
        l = 0; r = len(A) - 1
        while l <= r:
            m = (l + r)//2
            if A[m] == target:
                return True
            elif A[l] < A[m]:
                if A[l] <= target and target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif A[l] > A[m]:
                if A[m] < target and target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        
        return False
        
if __name__ == "__main__":
    test = Solution()
    A = [4, 4, 4, 4, 0, 1, 4]
    target = 1
    print test.search(A, target)