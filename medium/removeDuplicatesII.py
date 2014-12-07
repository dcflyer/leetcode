# -*- coding: utf-8 -*-
"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3], 

Your function should return length = 5, and A is now [1,1,2,2,3]. 

@author: n609874
"""
class Solution:
    # @param A a list of integers
    # @return an integer

# refresh removeDuplicates I !!!
# NOT A GOOD METHOD for removeDuplicates I, 
# i doesn't need to compare with i + 1, i can compare with j
#    def removeDuplicates(self, A):
#        if not A or 0 == len(A): return 0
#        
#        i, j = 0, 0
#        while i < len(A) - 1:
#            if A[i] == A[i + 1]:
#                i += 1
#            else:
#                i += 1
#                j += 1
#                A[j] = A[i]
#        return j + 1

#    def removeDuplicates(self, A):
#        if not A or 0 == len(A): return 0
#        
#        i, j = 0, 0
#        while i < len(A):
#            if A[i] != A[j]:
#                j += 1
#                A[j] = A[i]
#            i += 1
#        return j + 1

    def removeDuplicates(self, A):
        if not A: return 0
        if len(A) < 3: return len(A)        
        
        i, j = 0, 0
        count = 0
        for i in xrange(len(A)):
            if i > 0 and A[i] == A[i - 1]:
                count += 1
                if count > 2:
                    continue
            else:
                count = 1
#            WRONG !!!
#            j += 1
            A[j] = A[i]
            j += 1
            
        return j
        
        
if __name__ == "__main__":
    test = Solution()
    print test.removeDuplicates([1,1,1,2,2,2])
            