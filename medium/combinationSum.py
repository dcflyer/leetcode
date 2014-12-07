# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 18:39:16 2014
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3] 
@author: weichen
"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
#    def combinationSum(self, candidates, target):
#        self.res = []
##        the way to remove duplicates from a list
#        candidates = list(set(candidates))
#        candidates.sort()
#        item = []
#        self.combination(candidates, 0, target, item)
#        return self.res
#        
#    def combination(self, candidates, start, target, item):
#
#        if target < 0: return
#        if target == 0: self.res.append(item[:])
#
#        for i in xrange(start, len(candidates)):
#            if i != 0 and candidates[i] == candidates[i-1]:
#                continue
#            item.append(candidates[i])
#            self.combination(candidates, i, target - candidates[i], item)
#            item.pop()
            
    def combinationSum(self, candidates, target):
        self.res = []
        candidates.sort()
        item = []
        self.combination(candidates, target, item)
        return self.res
        
    def combination(self, candidates, target, item):

        if target < 0: return
        if target == 0: self.res.append(item[:])

        for i, c in enumerate(candidates):
#            don't remvoe duplicates, but skip them
            if i != 0 and c == candidates[i-1]:
                continue
            item.append(c)
            self.combination(candidates[i:], target - c, item)
            item.pop()            

if __name__ == "__main__":
    test = Solution()
    res = test.combinationSum([2, 3, 6, 7], 7)
    print res
    
        