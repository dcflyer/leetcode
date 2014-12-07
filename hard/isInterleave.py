# -*- coding: utf-8 -*-
"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

@author: Dennis
"""

class Solution:
    # @return a boolean
## 1. recursive (Time Limit Exceeded)
#    def isInterleave(self, s1, s2, s3):
#      if len(s1) + len(s2) != len(s3): return False
#      
#      return self.helper(s1, s2, s3)
#      
#    def helper(self, s1, s2, s3):
#        if not s3: return not s1 and not s2
#        if not s1: return s2 == s3
#        if not s2: return s1 == s3
#        
#        if s1[0] == s3[0] and s2[0] == s3[0]:
#            return self.helper(s1[1:], s2, s3[1:]) or \
#                    self.helper(s1, s2[1:], s3[1:])
#        elif s1[0] == s3[0]:
#            return self.helper(s1[1:], s2, s3[1:])
#        elif s2[0] == s3[0]:
#            return self.helper(s1, s2[1:], s3[1:])
#        else:
#            return False
            
## 2. DP time O(mn), space O(mn)
#    def isInterleave(self, s1, s2, s3):
#        if len(s1) + len(s2) != len(s3): return False
#        
#        dp = [[False for j in xrange(len(s2) + 1)] for i in xrange(len(s1) + 1)]
#        
#        dp[0][0] = True
#        for j in xrange(1, len(s2) + 1):
#            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
#                
#        for i in xrange(1, len(s1) + 1):
#            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
#            for j in xrange(1, len(s2) + 1):
#                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or \
#                    (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
#
#        
#        return dp[len(s1)][len(s2)]
        
# 3. DP time O(mn), space O(min(m,n))
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
            
        shortStr = s1 if len(s1) < len(s2) else s2
        longStr = s1 if len(s1) >= len(s2) else s2
        
        dp = [False for j in xrange(len(shortStr) + 1)]
        dp[0] = True
        for j in xrange(1, len(shortStr) + 1):
            dp[j] = dp[j - 1] and shortStr[j - 1] == s3[j - 1]
        
        for i in xrange(1, len(longStr) + 1):
            dp[0] = dp[0] and longStr[i - 1] == s3[i - 1]
            for j in xrange(1, len(shortStr) + 1):
                dp[j] = dp[j - 1] and shortStr[j - 1] == s3[i + j - 1] or \
                    (dp[j] and longStr[i - 1] == s3[i + j - 1])
        return dp[-1]
        
            
if __name__ == "__main__":
    test = Solution()
    s1 = "aabcc"; s2 = "dbbca"
    print test.isInterleave(s1, s2, "aadbbcbcac")
    print test.isInterleave(s1, s2, "aadbbbaccc")