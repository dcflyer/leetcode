# -*- coding: utf-8 -*-
"""
There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

@author: Dennis
"""

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if 1 == (lenA + lenB)%2:
            return self.getMedian(A, B, (lenA + lenB)/2 + 1)
        else:
            return ( self.getMedian(A, B, (lenA + lenB)/2) + \
                self.getMedian(A, B, (lenA + lenB)/2 + 1)) * .5
        
    def getMedian(self, A, B, k):
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getMedian(B, A, k)
        
        if 0 == lenA: return B[k - 1]
        if 1 == k: return min(A[0], B[0])
        pa = min(k/2, lenA); pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getMedian(A[pa:], B, k - pa)
        else:
            return self.getMedian(A, B[pb:], k - pb)

if __name__ == "__main__":
    test = Solution()
    print test.findMedianSortedArrays([2], [])
        
        
        