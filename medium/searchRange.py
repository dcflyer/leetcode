# -*- coding: utf-8 -*-
"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 

@author: n609874
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0; end = len(A) - 1
        range = [-1,-1]
        while start <= end:
            mid = (start + end)/2
            if A[mid] == target:
                range = [mid, mid]
#                WRONG !!! Didn't work on [8,8], 8 case
#                Don't wait for the next NOT MATCH, may go out of bound 
#                for i in xrange(mid, -1, -1):
#                    if A[i] != target:
#                        range[0] = i + 1
#                        break
#                for i in xrange(mid, len(A)):
#                    if A[i] != target:
#                        range[1] = i - 1
#                        break
                for i in xrange(mid, -1, -1):
                    if A[i] == target:
                        range[0] = i
                    else:
                        break
                for i in xrange(mid, len(A)):
                    if A[i] == target:
                        range[1] = i
                    else:
                        break
                break
            elif A[mid] < target:
                start = mid + 1
            elif A[mid] > target:
                end = mid - 1
        
        return range

if __name__ == "__main__":
    test = Solution()
    AList = [[5, 7, 7, 8, 8, 10], [8], [], [8, 8]]
    for A in AList:
        print test.searchRange(A, 8)
