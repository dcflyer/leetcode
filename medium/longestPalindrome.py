# -*- coding: utf-8 -*-
"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

@author: n609874
"""
class Solution:
    # @return a string
# 1. O(n^2) complexity and O(1) space
       
#    def longestPalindrome(self, s):
#        if not s: return ""
#        
#        p = s[0]        
#        for i in xrange(len(s)-1):
#            p1 = self.extendFromCenter(s, i, i)
#            if len(p1) > len(p): p = p1
#            p2 = self.extendFromCenter(s, i, i + 1)    
#            if len(p2) > len(p): p = p2                
#        
#        return p
#        
#    def extendFromCenter(self, s, i, j):
#        l = i; r = j        
#        while l >=0 and r <= len(s) - 1 and s[l] == s[r]:
#            l -= 1; r += 1
#        return s[l+1:r]
       
# 2. DP O(n^2) complexity and O(n^2) space
#    !!! Memory Limit Exceeded !!!
#     def longestPalindrome(self, s):
#         n = len(s)
#         if n < 1: return ""
#         p = [False for x in xrange(n)]
#         isP = [p[:] for x in xrange(n)]
#
#         maxLen = 1; start = 0; end = 0
#
# #        for i in xrange(n):
# #            for j in xrange(i):
# #                isP[j][i] = (s[j] == s[i]) and (i - j <= 2 or isP[j+1][i-1])
# #                if isP[j][i] and i - j + 1 > maxLen:
# #                    maxLen = i - j + 1
# #                    start = j
# #                    end = i
# #            isP[i][i] = True
# #        return s[start:end+1]
#
#         for i in xrange(n-1, -1, -1):
#             for j in xrange(i, n):
#                 isP[i][j] = (s[i] == s[j]) and (j - i <= 2 or isP[i+1][j-1])
#                 if isP[i][j] and j - i + 1 > maxLen:
#                     maxLen = j - i + 1
#                     start = i
#                     end = j
#         return s[start:end+1]

# 3.  Manacher's algorithm O(n) complexity and O(n) space
    def longestPalindrome(self, s):
        if not s: return ""
        new_s = "^"
        for c in s:
            new_s += "#" + c
        new_s += "#$"

        n = len(new_s); C = 0; R = 0
        P = [0]*n
        for i in xrange(1, n - 1):
            i_mirror = 2*C - i
            P[i] = min(R - i, P[i_mirror]) if R > i else 0

            while new_s[i + 1 + P[i]] == new_s[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        maxlen = 0
        C = 0
        for i in xrange(1, n - 1):
            if P[i] > maxlen:
                maxlen = P[i]
                C = i

        return s[(C - 1 - maxlen)//2:(C - 1 - maxlen)//2 + maxlen]

        
if __name__ == "__main__":
    test = Solution()
    print test.longestPalindrome("abb")
    print test.longestPalindrome("abacdfgdcaba")