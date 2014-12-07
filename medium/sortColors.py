# -*- coding: utf-8 -*-
"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue. 

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively. 

Note:
You are not suppose to use the library's sort function for this problem. 

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

@author: n609874
"""

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place

## 1. two flags, front and end
#    def sortColors(self, A):
#        if not A: return
#        
#        redFlag, blueFlag, i = -1, len(A), 0
##        WRONG !!! cannot use for loop, i should not increase when update blue
##        for i in xrange(len(A)):
##        WRONG !!! i should stop once it reaches blue block
##        while i < len(A):
#        while i < blueFlag:
#            if 0 == A[i]:
#                redFlag += 1
#                A[redFlag], A[i] = A[i], A[redFlag]
#                i += 1
#            elif 2 == A[i]:
#                blueFlag -= 1
#                A[blueFlag], A[i] = A[i], A[blueFlag]
#            else:
#                i += 1

# 2. maintain three window lengths, easy to extend to 4 or 5 windows
    def sortColors(self, A):
        if not A: return
        
        r, w, b = 0, 0, 0
        for i in xrange(len(A)):
            if 0 == A[i]:
                A[r], A[i] = A[i], A[r]
                if w > 0: A[r + w], A[i] = A[i], A[r + w]
#                if b > 0: A[r + w + b], A[i] = A[i], A[r + w + b]
                r += 1
            elif 1 == A[i]:
                A[r + w], A[i] = A[i], A[r + w]
#                if b > 0: A[r + w + b], A[i] = A[i], A[r + w + b]
                w += 1
            else:
                b += 1
        
        
if __name__ == "__main__":
    test = Solution()
    A = [0,2,2,1,0,0,1,2,1]
    test.sortColors(A)
    print A    