# -*- coding: utf-8 -*-
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 

@author: n609874
"""

class Solution:
    # @return an integer
    def reverse(self, x):
        nonnegate = x >= 0
        x = abs(x)
        y = 0
        while x > 0:
            r = x%10
            y = y*10 + r
            x = x/10
        return y if nonnegate else -y
        
if __name__ == "__main__":
    x = 123; y = -406; z = 300
    test = Solution()
    print test.reverse(x)
    print test.reverse(y)
    print test.reverse(z)
            
        
