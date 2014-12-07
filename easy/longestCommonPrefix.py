# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:27:40 2014

Write a function to find the longest common prefix string amongst an array of strings. 

@author: n609874
"""
#class Solution:
#    # @return a string
#    def longestCommonPrefix(self, strs):
#        lcp = ""
#        if len(strs) < 1:
#            return lcp
#        if len(strs) == 1:
#            return strs[0]
#        
#        i = 0
#        Findlcp = False
#        
#        while True:
#            temp = strs[0][i]
#            for s in strs:
#                if len(s) <= i or s[i] != temp:
#                    Findlcp = True
#                    break
#            if not Findlcp:
#                lcp += temp
#                i += 1
#            else:
#                break
#        
#        return lcp
# THE KEY POINT is to keep updaing the lcp
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        lcp = strs[0]
        for s in strs[1:]:
            # n = len(lcp)
            n = len(s)
            # for i, c in enumerate(s):            
            for i, c in enumerate(lcp):
                if i >= n or c != s[i]:
                    lcp = lcp[:i]
                    break
        return lcp


if __name__ == "__main__":
    test = Solution()
    strs = ["a", "b"]
    print test.longestCommonPrefix(strs)
    
                
        
            
            