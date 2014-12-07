# -*- coding: utf-8 -*-
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

@author: Dennis
"""

class Solution:
    # @return a string
    def minWindow(self, S, T):
        hashmap = dict((x, T.count(x)) for x in set(T))
        left, minWin, minleft, count = 0, len(S) + 1, 0, len(T)
        
        for right in xrange(len(S)):
            if S[right] in hashmap:
                hashmap[S[right]] -= 1
                if hashmap[S[right]] >= 0: count -= 1
            while 0 == count:
                if right - left + 1 < minWin:
                    minWin, minleft = right - left + 1, left
                    
                if S[left] in hashmap:
                    hashmap[S[left]] += 1
                    if hashmap[S[left]] > 0: count += 1
                left += 1
        
        if minWin > len(S): return ""
        else: return S[minleft:minleft + minWin]
            
if __name__ == "__main__":
    test = Solution()
    S = "ADOBECODEBANC"; T = "ABC"
    print test.minWindow(S, T)        
        