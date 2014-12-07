# -*- coding: utf-8 -*-
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

@author: n609874
"""
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if not num or len(num) < 3: return 0
        
        num.sort()
        close = sum(num[:3])
        
        for i in xrange(len(num) - 2):
            l, r = i + 1, len(num) - 1
            while l < r:
                s = num[i] + num[l] + num[r]
                if abs(s - target) < abs(close - target):
                    close = s
                if s == target:
                    return close                    
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return close

if __name__ == "__main__":
    test = Solution()
    print test.threeSumClosest([-3,-2,-5,3,-4], -1)
