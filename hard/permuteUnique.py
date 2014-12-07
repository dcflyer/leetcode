# -*- coding: utf-8 -*-
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations. 

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1]. 

@author: n609874
"""
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        self.res = []
        self.n = len(num)
        num.sort()
        used = [False for x in xrange(len(num))]
        item = []
        self.permutation(used, item, num)
        return self.res
        
    def permutation(self, used, item, num):
        if len(item) == self.n:
            self.res.append(item[:])
        
        for i in xrange(self.n):
            if i != 0 and not used[i-1] and num[i] == num[i-1]: 
                continue
            if not used[i]:
                item.append(num[i])
                used[i] = True
                self.permutation(used, item, num)
                item.pop()
                used[i] = False

if __name__ == "__main__":
    test = Solution()
    print test.permuteUnique([1,2,1])
    