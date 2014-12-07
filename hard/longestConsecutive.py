# -*- coding: utf-8 -*-
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

@author: Dennis
"""

class Solution:
    # @param num, a list of integer
    # @return an integer

## 1. remove item
#    def longestConsecutive(self, num):
#        maxLen = 0
#        if not num: return maxLen
#        intSet = set(num)
#        
#        while intSet:
#            item = intSet.pop()
#            currLen = 1
#            i = item + 1
#            while i in intSet:
#                currLen += 1
#                intSet.remove(i)
#                i += 1
#            i = item - 1
#            while i in intSet:
#                currLen += 1
#                intSet.remove(i)
#                i -= 1
#            maxLen = max(maxLen, currLen)
#        return maxLen

# 2. create visited 
    def longestConsecutive(self, num):
        maxLen = 0
        if not num: return maxLen
        intDict = {x: False for x in num}
        
        for item in intDict:
            if not intDict[item]:
                currLen = 1
                x = item + 1
                while x in intDict:
                    intDict[x] = True
                    currLen += 1
                    x += 1
                x = item - 1
                while x in intDict:
                    intDict[x] = True
                    currLen += 1
                    x -= 1
                maxLen = max(maxLen, currLen)
        return maxLen
                
if __name__ == "__main__":
    test = Solution()
    print test.longestConsecutive([100, 4, 200, 1, 3, 2])
                
        
        
        