# -*- coding: utf-8 -*-
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1]. 

Note:
Could you optimize your algorithm to use only O(k) extra space? 

@author: n609874
"""
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        row = []
        for i in xrange(0, rowIndex + 1):
            row.append(1)
            for j in xrange(i - 1, 0, -1):
                row[j] += row[j-1]
        return row

if __name__ == "__main__":
    test = Solution()
    for i in xrange(1, 6):
        print test.getRow(i)
