# -*- coding: utf-8 -*-
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135", 

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 

@author: n609874
"""

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.res = []
        if not s: return self.res
        
        self.helper("", s, 0)
        return self.res
    
    def helper(self, currIP, currS, currIndex):
        if 3 == currIndex:
            if len(currS):
                if str(int(currS)) == currS and int(currS) <= 255:
                    self.res.append(currIP + currS)
            return
        
        for i in xrange(1, 4):
            if len(currS) >= i and str(int(currS[:i])) == currS[:i] and int(currS[:i]) <= 255:
                self.helper(currIP + currS[:i] + ".", currS[i:], currIndex + 1)
        
    
if __name__ == "__main__":
    test = Solution()
    res = test.restoreIpAddresses("25525511135")
    print res
        