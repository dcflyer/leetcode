# -*- coding: utf-8 -*-
"""
    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

@author: weichen
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num: return -1
        
        l, r = 0, len(num) - 1
        min = num[0]
        while l <= r:
            m = (l + r)//2
            if num[l] < num[m]:
                min = min if num[l] > min else num[l]
                l = m + 1
            elif num[l] > num[m]:
                min = min if num[m] > min else num[m]
                r = m - 1
            else:
                min = min if num[m] > min else num[m]
                l += 1
        
        return min
                
if __name__ == "__main__":
    test = Solution()
    num = [2, 1]
    print test.findMin(num)         
        
        
