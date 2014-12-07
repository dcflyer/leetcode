# -*- coding: utf-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

@author: n609874
"""
class Solution:
    # @param n, an integer
    # @return an integer
#    def climbStairs(self, n):
#        if n <= 1: return 1
#        
#        return self.climbStairs(n-1) + self.climbStairs(n-2)
    def climbStairs(self, n):
        if n <= 1: return 1
        
        ways = [1,1]
        for i in xrange(2, n+1):
            ways.append(ways[i-1] + ways[i-2])
        
        return ways[n]
        
    
if __name__ == "__main__":
    test = Solution()
    print test.climbStairs(3)
            
            