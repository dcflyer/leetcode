# -*- coding: utf-8 -*-
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
  
@author: Dennis
"""

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.res = []
        if not s: return self.res
        
        self.dp = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        for j in xrange(len(s)):
            for i in reversed(xrange(j + 1)):
                if s[i] == s[j] and (j - i < 2 or self.dp[i + 1][j - 1]):
                    self.dp[i][j] = True
        
        self.helper(0, [], s)
        return self.res
        
    def helper(self, start, partition, s):
        if start == len(s):
            self.res.append(partition)
            return
            
        for end in xrange(start, len(s)):
            if self.dp[start][end]:
                self.helper(end + 1, partition[:] + [s[start:end + 1]], s)

if __name__ == "__main__":
    test = Solution()
    print test.partition("aab")            
            
        