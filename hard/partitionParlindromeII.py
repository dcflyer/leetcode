# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 23:05:47 2014
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

@author: Dennis
"""

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if not s: return 0
        
        dp = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        for j in xrange(len(s)):
            for i in reversed(xrange(j + 1)):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        
#        res[i] saves the number of cuts in substring before ith char
        res = [0]*(len(s) + 1)
        for j in xrange(0, len(s)):
            res[j + 1] = j + 1
            for i in xrange(j + 1):
                if dp[i][j]:
                    res[j + 1] = min(res[j + 1], res[i] + 1)
        return res[len(s)] - 1

if __name__ == "__main__":
    test = Solution()
#    print test.minCut("aab")
    print test.minCut("bb")   