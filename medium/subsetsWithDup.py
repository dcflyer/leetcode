# -*- coding: utf-8 -*-
"""
Given a collection of integers that might contain duplicates, S, return all possible subsets. 

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example,
If S = [1,2,2], a solution is: 

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

@author: n609874
"""
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer

## !. recursive
#    def subsetsWithDup(self, S):
#        self.res = [[]]
#        if not S: return self.res
#        
#        S.sort()
#        sub = []
#        self.generate(0, S, sub)
#        return self.res
#    
#    def generate(self, start, S, sub):
#        for i in xrange(start, len(S)):
#            if i != start and S[i] == S[i - 1]:
#                continue
#            else:
#                sub.append(S[i])
#                self.res.append(sub[:])
#                if i < len(S) - 1:
#                    self.generate(i + 1, S, sub)
#                sub.pop()
        
## 2. iterative
#    WRONG !!! only consider two adjacent same numbers
#    def subsetsWithDup(self, S):
#        res = [[]]
#        if not S: return res
#        
#        S.sort()
#        for i in xrange(len(S)):
#            n = len(res)
##            WRONG!!! when n is odd, only the first one 
##            start = n//2 if i > 0 and S[i] == S[i - 1] else 0
#            start = n//2 + n%2 if i > 0 and S[i] == S[i - 1] else 0
#            curr = []
#            for j in xrange(start, n):
#                copy = res[j][:]
#                copy.append(S[i])
#                curr.append(copy)
#            res += curr
#        
#        return res
    def subsetsWithDup(self, S):
        res = [[]]
        if not S: return res
        
        S.sort()
        start = 0
        for i in xrange(len(S)):
            size = len(res)
            for j in xrange(start, size):
                copy = res[j][:]
                copy.append(S[i])
                res.append(copy)
            if i < len(S) - 1 and S[i] == S[i + 1]:
                start = size
            else:
                start = 0
        
        return res
                

if __name__ == "__main__":
    test = Solution()
    S = [5,5,5,5]
    print test.subsetsWithDup(S)
                
                
        
