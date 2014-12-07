# -*- coding: utf-8 -*-
"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

@author: Dennis
"""

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer

# time complexity O(n), space complexity O(L)
    def findSubstring(self, S, L):
        res = []
        if not S or not L: return res
        
        lenS, lenL, lenWord = len(S), len(L), len(L[0])
#        !!!!! anther way to generate a dict !!!!!
        hashmap = dict((x, L.count(x)) for x in set(L))
#        hashmap = {}
#        for i in xrange(lenL):
#            hashmap[L[i]] = hashmap.get(L[i], 0) + 1
        
        for i in xrange(lenS - lenL*lenWord + 1):
            newhashmap = {}; j = 0
#            WRONG, if we want to use j, while loop is better
#            for j in xrange(lenL):
            while j < lenL:
                sub = S[i + j*lenWord:i + j*lenWord + lenWord]
                if sub not in hashmap:
                    break
                else:
                    newhashmap[sub] = newhashmap.get(sub, 0) + 1
                    if newhashmap[sub] > hashmap[sub]: break
                    j += 1
            if j == lenL: res.append(i)
        return res     
        
if __name__ == "__main__":
    test = Solution()
    S = "barfoothefoobarman"
    L = ["foo", "bar"]
    print test.findSubstring(S, L)        