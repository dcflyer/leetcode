# -*- coding: utf-8 -*-
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2]. 

@author: weichen
"""
class Solution:
    # @param a list of integers
    # @return an integer
#    def removeDuplicates(self, A):
#        if len(A) < 2:
#            return len(A)
#        i = 1
#        while i < len(A):
#            if A[i] != A[i-1]:
#                i = i + 1
#            else:
#                A.pop(i)
#
#        return i

    def removeDuplicates(self, A):
        if len(A) == 1:
            return 1
        i = 0; j = 0
        while j < len(A):
            if A[j] != A[i]:
                i = i + 1
                A[i] = A[j]
            j = j + 1
        return i + 1
    
        
if __name__ == "__main__":
    
    A = [2,1,3,2,4,2,1,5,6,1,3]
    A.sort()
    B = [1,1,1,1]
    test = Solution()
    print test.removeDuplicates(A)
    print A
    print test.removeDuplicates(B)
    print B

