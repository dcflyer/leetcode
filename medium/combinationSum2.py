# -*- coding: utf-8 -*-
"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6] 
@author: weichen
"""
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        self.res = []
        item = []
        candidates.sort()
        self.combination(candidates, target, item)
        return self.res
        
    def combination(self, candidates, target, item):
        if target < 0: return
        if target == 0: self.res.append(item[:])
            
        for i, c in enumerate(candidates):
            if i != 0 and c == candidates[i-1]:
                continue
            item.append(c)
            self.combination(candidates[i+1:], target - c, item)
            item.pop()

if __name__ == "__main__":
    test = Solution()
    res = test.combinationSum2([10,1,2,7,6,1,5], 8)
    print res
            