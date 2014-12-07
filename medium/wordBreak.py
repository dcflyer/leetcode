# -*- coding: utf-8 -*-
"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words. 

For example, given
s = "leetcode",
dict = ["leet", "code"]. 

Return true because "leetcode" can be segmented as "leet code". 

@author: n609874
"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        res = [False for x in xrange(len(s)+1)]
        res[0] = True
        for i in xrange(1, len(s)+1):
            sub_s = s[:i]
            for j in xrange(i):
                if res[j] and sub_s[j:] in dict:
                    res[i] = True
                    break
        
        return res[-1]
    
if __name__ == "__main__":
    test = Solution()
#    s = "leetcode"
#    dict = ["leet", "code"]
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print test.wordBreak(s, dict)