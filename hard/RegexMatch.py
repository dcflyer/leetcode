# -*- coding: utf-8 -*-
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

@author: Dennis
"""

class Solution:
    # @return a boolean
## 1. recursive method (Time Limit Exceeded)
#    def isMatch(self, s, p):
#        if not p: return not s
#        if 1 == len(p) or '*' != p[1]:
##            WRONG !!!
##            if not s or s[0] != p[0] or '.' != p[0]:
#            if not s or (s[0] != p[0] and '.' != p[0]):
#                return False
#            return self.isMatch(s[1:], p[1:])
#        i = -1
#        while i < len(s) and i < 0 or '.' == p[0] or s[i] == p[0]:
#            if self.isMatch(s[i + 1:], p[2:]):
#                return True
#            i += 1
#        return False

# 2. DP method
    def isMatch(self, s, p):
        dp = [[False for i in xrange(len(p) + 1)] for j in xrange(len(s) + 1)]
        dp[0][0] = True
#        how to match empty substring of s from p
        for i in xrange(1, len(p) + 1):
            if '*' == p[i - 1]:
                if i > 1:
                    dp[0][i] = dp[0][i - 2]                 
        
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if '.' == p[j - 1]:     # the jth entry in p is .
                    dp[i][j] = dp[i - 1][j - 1]
                elif '*' == p[j - 1]:   # the jth entry in p is *
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or \
                        (dp[i - 1][j] and (s[i - 1] == p[j - 2] or '.' == p[j - 2]))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[len(s)][len(p)]
   
if __name__ == "__main__":
    test = Solution()
    print test.isMatch("aab", "c*a*b")
        
        