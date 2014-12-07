# -*- coding: utf-8 -*-
"""
Given a set of distinct integers, S, return all possible subsets. 

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If S = [1,2,3], a solution is: 

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

@author: n609874
"""

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
# NP hard problem
# !. recursive
# NOT GOOD ENOUGH, not a real recursive method
#    def subsets(self, S):
#        self.res = [[]]
#        if not S: return self.res
#        n = len(S)        
#        S.sort()
#        return self.subAdd(n, S)
#    
#    def subAdd(self, n, S):
#        if 0 == n:
#            return [[]]
#        
#        curr = self.subAdd(n - 1, S)
#        prev = []
#        for x in curr:
#            copy_x = x[:]
#            copy_x.append(S[n - 1])
#            prev.append(copy_x)
#        curr += prev
#        
#        return curr

    def subsets(self, S):
        self.res = [[]]
        if not S: return self.res
        S.sort()
        sub = []
        self.generate(0, S, sub)
        
        return self.res
    
    def generate(self, start, S, sub):
        for i in xrange(start, len(S)):
            sub.append(S[i])
            self.res.append(sub[:])
            if i < len(S) - 1:
                self.generate(i + 1, S, sub)
            sub.pop()
        
# 2. iterative 
#    def subsets(self, S):
#        res = [[]]
#        if not S: return res
#        
#        S.sort()
#        for i, c in enumerate(S):
#            curr = []
#            for x in res:
#                copy_x = x[:]
#                copy_x.append(c)
#                curr.append(copy_x)
#            res += curr
#        
#        return res
        
if __name__ == "__main__":
    test = Solution()
    S = [1,2,3]
    print test.subsets(S)
            
        
        
        
        
        