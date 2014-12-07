# -*- coding: utf-8 -*-
"""
Given an array of integers, every element appears three times except for one. Find that single one. 

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

@author: n609874
"""
class Solution:
    # @param A, a list of integer
    # @return an integer

##1. Doesn't work on python, negative numbers are presented differently
#    def singleNumber(self, A):
#        digits = [0]*32
#        res = 0
#        for i in xrange(32):
#            for j in xrange(len(A)):
#                digits[i] += (A[j] >> i)&1
#            res |= digits[i]%3 << i
#            
#        return res

##2. use mask
#    def singleNumber(self, A):
#        one, two = 0, 0
#        
#        for x in A:
#            two |= one & x      # add twice appearances to two
#            one ^= x            # remove twice appearances from one
#            three = one & two   # mark three appearances
#            one &= ~three       # remove three appearances from one
#            two &= ~three       # remove three appearances from two
#            
#        return one

#3. mask method from mitbbs 
#整体思路是：整数的32个bits，出现次数mod 3后必余0, 1, 2. 其中余1的就是答案
    def singleNumber(self, A):
        one, two = 0, 0
        for x in A:
#            WRONG !!!
#            zero = one & two
            zero = ~(one | two)
            two = (one & x) | (two & ~x)
            one = (one & ~x) | (zero & x)
        return one


if __name__ == "__main__":
    test = Solution()
#    print test.singleNumber([2,5,2,4,4,5,4,7,5,2])
#    print test.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
    test.singleNumber([4,4,4,2])

  