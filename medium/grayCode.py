# -*- coding: utf-8 -*-
"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined. 

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

@author: n609874
"""

class Solution:
    # @return a list of integers

# time complexity O(2^n), space complexity O(2^n)
## 1. two loops, not good enough for Python
#    def grayCode(self, n):
#        if n < 0: return []
#        res = [0]
#
##        start with 0 bit, go to n bits, n iterations
#        for i in xrange(n):
#            for j in reversed(xrange(len(res))):
##                WRONG !!! + is prior to <<
##                res.append(1 << i + res[j])
#                res.append((1 << i) + res[j])
#        return res

# 2. concise code of Python
    def grayCode(self, n):
        if n < 0: return []
        res = [0]

        for i in xrange(n):
            res += [ x + (1 << i) for x in res[::-1]]
        return res
        
if __name__ == "__main__":
    test = Solution()
    print test.grayCode(2)        
        
        