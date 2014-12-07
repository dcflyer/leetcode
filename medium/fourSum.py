# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

@author: n609874
"""
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]

# complexity O(n^3), (Time Limit Exceeded)         
#    def fourSum(self, num, target):
#        res = []
#        n = len(num)
#        if n < 4: return res
#        num.sort()
#        
#        for i in xrange(n - 3):
#            if i != 0 and num[i] == num[i - 1]:
#                continue
#            for j in xrange(i + 1, n - 2):
#                if j != i + 1 and num[j] == num[j - 1]:
#                    continue
#                l, r = j + 1, n - 1
#                while l < r:
#                    s = num[i] + num[j] + num[l] + num[r]
#                    if s == target:
#                        res.append([num[i], num[j], num[l], num[r]])
#                        l += 1; r -= 1
##                        WRONG!!! check index out of bounds
##                        while num[l] == num[l - 1]: l += 1
##                        while num[r] == num[r + 1]: r -= 1    
#                        while l < r and num[l] == num[l - 1]: l += 1
#                        while l < r and num[r] == num[r + 1]: r -= 1    
#                    elif s < target:
#                        l += 1
#                    else:
#                        r -= 1
#        return res

    def fourSum(self, num, target):
        n, res, twopair = len(num), set(), {}
        
        if n < 4: return []
        num.sort()
        for i in xrange(n - 1):
            for j in xrange(i + 1, n):
                s = num[i] + num[j] 
                if not s in twopair:
                    twopair[s] = [(i, j)]
                else:
                    twopair[s].append((i, j))
        
        for i in xrange(n - 3):
            for j in xrange(i + 1, n - 2):
                s = target - num[i] - num[j]
                if s in twopair:
                    for k in twopair[s]:
                        if k[0] > j:
                            res.add((num[i], num[j], num[k[0]], num[k[1]]))
        return [list(x) for x in res]

if __name__ == "__main__":
    test = Solution()
    print test.fourSum([1, 0, -1, 0, -2, 2], 0)
    print test.fourSum([0, 0, 0, 0], 0)
        
        
        
