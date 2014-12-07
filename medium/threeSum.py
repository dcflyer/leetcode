# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

@author: n609874
"""
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]

# not good enough (Time Limit Exceeded)
#    def threeSum(self, num):
#        if not num: return []
#        
#        self.res = []
#        num.sort()
#        item = []      
#        self.threehelper(num, item)
#        return self.res
#        
#    def threehelper(self, num, item):
#        if len(item) == 3:
#            if not sum(item): self.res.append(item[:])
#            return
#        if not num: return
#
#        for i, c in enumerate(num):
#            if i > 0 and c == num[i - 1]:
#                continue
#            item.append(c)
#            self.threehelper(num[i+1:], item)
#            item.pop()
            
# complexity O(n^2), if used DP above, exponential complexity            
    def threeSum(self, num):
        res = []
        if not num or len(num) < 3: return res
        num.sort()
    
        for i in xrange(len(num) - 2):
            if i != 0 and num[i] == num[i - 1]:
                continue
            
            l, r = i + 1, len(num) - 1
            while l < r:
                s = num[i] + num[l] + num[r] 
                if 0 == s:
                    res.append([num[i], num[l], num[r]])
                    l += 1; r -= 1
                    while l < r and num[l] == num[l - 1]: l += 1
                    while l < r and num[r] == num[r + 1]: r -= 1
                elif 0 < s:
                    r -= 1
                else:
                    l += 1
        return res
        
if __name__ == "__main__":
    test = Solution()
    print test.threeSum([-1, 0, 1, 2, -1, -4])
        
