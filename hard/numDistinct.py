# -*- coding: utf-8 -*-
"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

@author: Dennis
"""

#无论T的字符与S的字符是否匹配，dp[i][j] = dp[i][j - 1].就是说，假设S已经匹配了j - 1个字符，得到匹配个数为dp[i][j - 1].
#现在无论S[j]是不是和T[i]匹配，匹配的个数至少是dp[i][j - 1].
#除此之外，当S[j]和T[i]相等时，我们可以让S[j]和T[i]匹配，然后让S[j - 1]和T[i - 1]去匹配.

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if not T: return 1
        if not S: return 0
            
        dp = [[0 for j in xrange(len(S) + 1)] for i in xrange(len(T) + 1)]
        for j in xrange(len(S) + 1):
            dp[0][j] = 1
        for j in xrange(1, len(S) + 1):
            for i in xrange(1, len(T) + 1):
                dp[i][j] = dp[i][j - 1] + (dp[i - 1][j - 1] if T[i - 1] == S[j - 1] else 0)
        
        return dp[len(T)][len(S)]
        
if __name__ == "__main__":
    test = Solution()
    print test.numDistinct("rabbbit", "rabbit")        
        