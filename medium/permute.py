# -*- coding: utf-8 -*-
"""
Given a collection of numbers, return all possible permutations. 

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 

@author: n609874
"""
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
# 1. recursive method
#    def permute(self, num):
#        self.res = []
#        self.n = len(num)
#        item = []
#        used = [False for x in xrange(self.n)]
#        self.permutation(used, item, num)
#        return self.res
#    
#    def permutation(self, used, item, num):
#        if len(item) == self.n:
#            self.res.append(item[:])
#        
#        for i, c in enumerate(num):
#            if used[i] == False:
#                used[i] = True
#                item.append(c)
#                self.permutation(used, item, num)
#                item.pop()
#                used[i] = False

# 2. iterative method
    def permute(self, num):
        if len(num) == 0: return []
        res = [[num[0]]]
        for c in num[1:]:
            new_res = []
            for x in res:
                for pos in xrange(len(x) + 1):
                    new_x = x[:]
                    new_x.insert(pos, c)
                    new_res.append(new_x)
            res = new_res
        return res
                
if __name__ == "__main__":
    test = Solution()
    print test.permute([1,2,3])