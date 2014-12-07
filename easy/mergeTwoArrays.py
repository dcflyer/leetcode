# -*- coding: utf-8 -*-
"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

@author: n609874
"""
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m - 1; j = n - 1
        end = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] <= B[j]:
                A[end] = B[j]
                j = j - 1
            else:
                A[end] = A[i]
                i = i - 1
            end = end - 1
        if i < 0:
            for k in xrange(j, -1, -1):
                A[end] = B[k]
                end = end - 1

if __name__ == "__main__":
    A = [1,3,5,7,9,0,0,0,0,0]
    B = [2,4,6,8,10]
    test = Solution()
    test.merge(A, 5, B, 5)
    print A
