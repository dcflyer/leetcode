# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 11:13:15 2014
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3): 

1."123"
2."132"
3."213"
4."231"
5."312"
6."321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

@author: n609874
"""

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        res = ""
        if n <= 0: return res
        
#        calculate (n - 1)!
        fac = 1
        for i in xrange(1, n):
            fac *= i
            
        k -= 1 # !!!!! the index start from 0    
        num = range(1, n + 1) #
        for i in reversed(xrange(1, n)):
            curr = num[k / fac]
            res += str(curr)
            num.remove(curr)
#            k should updated before fac
#            fac /= i
#            k %= fac
            k %= fac
            fac /= i            
            
#        WRONG !!! there are n number, but only n - 1 iterations in above loop
#        add the last one to string in the end
        res += str(num[0])
        return res

if __name__ == "__main__":
    test = Solution()
    print test.getPermutation(3, 2)
            
            
            
    