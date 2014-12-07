# -*- coding: utf-8 -*-
"""
Implement pow(x, n). 

@author: weichen
"""
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
#    def pow(self, x, n):
#        if n == 0: return 1
#        
#        if n < 0:
#            return 1/self.pow(x, -n)
#        else:
#            t = self.pow(x, n/2)
#            if not n%2: 
#                return t*t
#            else:
#                return t*t*x

# This one is quicker!!!
    def pow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1/self.pow(x, -n)
        elif n % 2:
            return self.pow(x*x,n/2)*x
        else:
            return self.pow(x*x,n/2)                
                
if __name__ == "__maiin__":
    test = Solution()
    print test.pow(8.88023, 3)
