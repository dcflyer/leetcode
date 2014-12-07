# -*- coding: utf-8 -*-
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

@author: weichen
"""
class Solution:
    # @return a list of lists of integers
#    def combine(self, n, k):
#        self.res = []
#        item = []
#        self.combination(range(1, n + 1), k, item)
#        return self.res
#    
#    def combination(self, currSet, k, item):
#        
#        if k == 0: 
##            WRONG!!!!!!
##            self.res.append(item)
#            self.res.append(item[:])
#            return
#            
#        for i, c in enumerate(currSet):
#            item.append(c)
#            self.combination(currSet[i+1:], k-1, item)
#            item.pop()

    def combine(self, n, k):
        self.res = []
        self.k = k
        item = []
        self.combination(1, n, item)
        return self.res
    
    def combination(self, s, n, item):
        if len(item) == self.k:
            self.res.append(item[:])

        for i in xrange(s, n + 1):
            item.append(i)
#            WRONG!!!!!
#            self.combination(s + 1, n, item)
            self.combination(i + 1, n, item)
            item.pop()
        
        
        
        
if __name__ == "__main__":
    test = Solution()
    res = test.combine(4, 2)        
    print res        